from pathlib import Path

import pandas as pd


class CSVProcessor:
    """
    Handles CSV processing using Pandas.
    """

    def summarize_csv(self, csv_path):
        """
        Read CSV and return basic summary.

        Args:
            csv_path (str or Path)

        Returns:
            dict
        """

        csv_path = Path(csv_path)

        if not csv_path.exists():
            raise FileNotFoundError(
                f"CSV file not found: {csv_path}"
            )

        try:

            df = pd.read_csv(csv_path)

            summary = {
                "rows": df.shape[0],
                "columns": df.shape[1],
                "column_names": list(df.columns),
                "preview": df.head().to_string(index=False),
                "full_text": df.to_string(index=False)
            }

            return summary

        except Exception as e:
            raise RuntimeError(
                f"Failed to process CSV: {e}"
            )