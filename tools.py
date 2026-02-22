from metrics import record_tool_call

def calculate_sip(monthly_investment: float, years: int, expected_return: float):
    record_tool_call("calculate_sip")
    r = expected_return / 100 / 12
    n = years * 12
    future_value = monthly_investment * ((1 + r)**n - 1) / r * (1 + r)
    return round(future_value, 2)

def vpn_troubleshoot(issue: str):
    record_tool_call("vpn_troubleshoot")
    return f"Try restarting the VPN app and checking your internet connection. Issue reported: {issue}"
