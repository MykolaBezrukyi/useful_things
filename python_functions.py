def write_json_file(file_path: str, data: Any) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        return json.dump(data, file)


def load_json_data(file_path: str) -> Any:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_file_as_string(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def extract_excel_dataframes(excel_file: pd.ExcelFile) -> dict[str, pd.DataFrame]:
    return {
            sheet_name: excel_file.parse(sheet_name, skiprows=[0])
            for sheet_name in excel_file.sheet_names
    }


def write_dataframes_to_excel(file_path: str, dataframes: dict[str, pd.DataFrame]) -> None:
    with pd.ExcelWriter(file_path) as excel_writer:
        for k, v in dataframes.items():
            v.to_excel(excel_writer, sheet_name=k, startrow=1, index=False)

