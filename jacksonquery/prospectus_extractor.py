import file_parser
import fee_extractor
import returns_extractor
import tenure_extractor
import turnover_extractor

# Constants
PROSPECTUS_FILEPATH = '../data/jackson_prospectus.pdf'


def run_prospectus_extractor(class_type='A'):
    string_list = file_parser.parse_file(PROSPECTUS_FILEPATH)
    subaccount_names = file_parser.parse_names(string_list)
    sublists = file_parser.split_into_sublists(string_list, subaccount_names)
    management_fees = fee_extractor.extract_management_fee(sublists)
    returns_class_A, returns_class_I = returns_extractor.extract_returns(sublists, subaccount_names)
    manager_tenures = tenure_extractor.extract_tenures(sublists)
    portfolio_turnovers = turnover_extractor.extract_avg_turnover(subaccount_names, PROSPECTUS_FILEPATH, class_type)

    return management_fees, returns_class_A, returns_class_I, manager_tenures, portfolio_turnovers


if __name__ == "__main__":
    fees, returns_A, returns_I, tenures, turnovers = run_prospectus_extractor()
