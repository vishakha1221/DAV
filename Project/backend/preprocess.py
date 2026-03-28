from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import pandas as pd

FEATURE_COLUMNS = ["studytime", "failures", "absences", "G1", "G2"]
TARGET_COLUMN = "G3"
GOOD_THRESHOLD = 10.0
GOOD_PERFORMANCE_LABEL = "Good Performance"
NEEDS_IMPROVEMENT_LABEL = "Needs Improvement"


def _normalize_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Strip whitespace from column names so the notebook and API stay aligned."""

    dataframe = dataframe.copy()
    dataframe.columns = [str(column).strip() for column in dataframe.columns]
    return dataframe


def _coerce_numeric_features(dataframe: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Convert selected columns to numeric values and keep a predictable order."""

    converted = dataframe.copy()
    for column in columns:
        converted[column] = pd.to_numeric(converted[column], errors="coerce")
    return converted[columns]


def load_dataset(data_path: str | Path) -> pd.DataFrame:
    """Load the student dataset from disk."""

    return pd.read_csv(data_path)


def prepare_training_frame(raw_frame: pd.DataFrame) -> pd.DataFrame:
    """Clean the training data by handling missing values and column names."""

    frame = _normalize_columns(raw_frame)

    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]
    missing_columns = [column for column in required_columns if column not in frame.columns]
    if missing_columns:
        missing_list = ", ".join(missing_columns)
        raise ValueError(f"Dataset is missing required column(s): {missing_list}")

    cleaned = _coerce_numeric_features(frame[required_columns], required_columns)

    for column in FEATURE_COLUMNS:
        median_value = cleaned[column].median()
        cleaned[column] = cleaned[column].fillna(median_value)

    cleaned = cleaned.dropna(subset=[TARGET_COLUMN]).reset_index(drop=True)
    return cleaned


def build_training_data(raw_frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Create the model feature matrix and the Good/Bad target labels."""

    cleaned = prepare_training_frame(raw_frame)
    features = cleaned[FEATURE_COLUMNS].copy()
    target = cleaned[TARGET_COLUMN].apply(
        lambda grade: GOOD_PERFORMANCE_LABEL if float(grade) >= GOOD_THRESHOLD else NEEDS_IMPROVEMENT_LABEL
    )
    return features, target


def validate_prediction_payload(payload: Mapping[str, Any]) -> None:
    """Raise a readable error when the prediction request is incomplete or invalid."""

    missing_columns = [column for column in FEATURE_COLUMNS if column not in payload or payload[column] in (None, "")]
    if missing_columns:
        missing_list = ", ".join(missing_columns)
        raise ValueError(f"Missing required input(s): {missing_list}")


def preprocess_record(record: Mapping[str, Any]) -> pd.DataFrame:
    """Convert one JSON request into the exact feature order used during training."""

    validate_prediction_payload(record)
    frame = pd.DataFrame([{column: record[column] for column in FEATURE_COLUMNS}])
    frame = _coerce_numeric_features(frame, FEATURE_COLUMNS)

    invalid_columns = [column for column in FEATURE_COLUMNS if pd.isna(frame.at[0, column])]
    if invalid_columns:
        invalid_list = ", ".join(invalid_columns)
        raise ValueError(f"Invalid numeric input(s): {invalid_list}")

    return frame
