from metrics import record_tool_call

def calculate_sip(monthly_investment: float, years: int, expected_return: float):
    record_tool_call("calculate_sip")
    r = expected_return / 100 / 12
    n = years * 12
    future_value = monthly_investment * ((1 + r)**n - 1) / r * (1 + r)
    return round(future_value, 2)
    
def calculate_emi(principal: float, annual_rate: float, tenure_years: int):
    record_tool_call("calculate_emi")
    r = annual_rate / 100 / 12
    n = tenure_years * 12

    if r == 0:
        emi = principal / n
    else:
        emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)

    return round(emi, 2)


def calculate_ltcg_india(sale_price: float, purchase_price: float, expenses: float = 0):
    record_tool_call("calculate_ltcg_india")
    capital_gain = sale_price - purchase_price - expenses
    taxable_gain = max(capital_gain, 0)

    # LTCG tax calculation at 12.5% (without indexation)
    tax = taxable_gain * 0.125

    return {
        "capital_gain": round(capital_gain, 2),
        "taxable_gain": round(taxable_gain, 2),
        "tax": round(tax, 2)
    }


def calculate_future_value(
    present_value: float,
    annual_rate: float,
    years: int
):
    record_tool_call("calculate_future_value")
    r = annual_rate / 100
    future_value = present_value * (1 + r) ** years

    return round(future_value, 2)


def calculate_cagr(
    initial_value: float,
    final_value: float,
    years: float
):
    record_tool_call("calculate_cagr")

    if initial_value <= 0 or years <= 0:
        return 0.0

    cagr = ((final_value / initial_value) ** (1 / years) - 1) * 100

    return round(cagr, 2)


def calculate_real_return(
    nominal_return: float,
    inflation_rate: float
):
    record_tool_call("calculate_real_return")

    real_return = (
        ((1 + nominal_return / 100) /
         (1 + inflation_rate / 100)) - 1
    ) * 100

    return round(real_return, 2)


def calculate_npv(
    initial_investment: float,
    cash_flows: list[float],
    discount_rate: float
):
    record_tool_call("calculate_npv")

    r = discount_rate / 100

    npv = -initial_investment

    for year, cash_flow in enumerate(cash_flows, start=1):
        npv += cash_flow / ((1 + r) ** year)

    return round(npv, 2)


def calculate_irr(
    initial_investment: float,
    cash_flows: list[float]
):
    record_tool_call("calculate_irr")

    cash_flows = [-initial_investment] + cash_flows

    def npv(rate):
        return sum(
            cash_flow / ((1 + rate) ** period)
            for period, cash_flow in enumerate(cash_flows)
        )

    low = -0.9999
    high = 10.0

    for _ in range(100):
        mid = (low + high) / 2

        if npv(mid) > 0:
            low = mid
        else:
            high = mid

    irr = ((low + high) / 2) * 100

    return round(irr, 2)


def calculate_fd_maturity(
    principal: float,
    annual_rate: float,
    tenure_years: float,
    compounding_frequency: int = 4
):
    record_tool_call("calculate_fd_maturity")

    r = annual_rate / 100
    n = compounding_frequency
    t = tenure_years

    maturity_amount = principal * (
        1 + r / n
    ) ** (n * t)

    interest_earned = maturity_amount - principal

    return {
        "maturity_amount": round(maturity_amount, 2),
        "interest_earned": round(interest_earned, 2)
    }


def calculate_income_tax_new_regime(
    annual_income: float
):
    record_tool_call("calculate_income_tax_new_regime")

    income = max(annual_income, 0)

    # New tax regime slabs (FY 2025-26 / AY 2026-27)
    slabs = [
        (400000, 0.00),
        (400000, 0.05),
        (400000, 0.10),
        (400000, 0.15),
        (400000, 0.20),
        (400000, 0.25),
        (float("inf"), 0.30)
    ]

    tax = 0
    remaining_income = income

    for slab_amount, rate in slabs:
        taxable_amount = min(remaining_income, slab_amount)
        tax += taxable_amount * rate
        remaining_income -= taxable_amount

        if remaining_income <= 0:
            break

    # 4% Health & Education Cess
    cess = tax * 0.04
    total_tax = tax + cess

    return {
        "income": round(income, 2),
        "income_tax": round(tax, 2),
        "cess": round(cess, 2),
        "total_tax": round(total_tax, 2)
    }


def apply_section_54_exemption(
    capital_gain: float,
    amount_invested_in_new_house: float
):
    record_tool_call("apply_section_54_exemption")

    exemption = min(
        max(capital_gain, 0),
        max(amount_invested_in_new_house, 0)
    )

    taxable_gain = max(capital_gain - exemption, 0)

    return {
        "capital_gain": round(capital_gain, 2),
        "section_54_exemption": round(exemption, 2),
        "taxable_gain": round(taxable_gain, 2)
    }
def vpn_troubleshoot(issue: str):
    record_tool_call("vpn_troubleshoot")
    return f"Try restarting the VPN app and checking your internet connection. Issue reported: {issue}"
