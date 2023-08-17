#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import re
import requests

def check_eligibility(address):
    eligible_check = f"https://incentivized-testnet.seinetwork.io/check-eligibility?seiAddress={address}"
    response = requests.get(eligible_check)
    response_json = response.json()
    return response_json
    
def sei_amount(number_usei):
    useiexponent = 6
    sei_amount = number_usei / (10 ** useiexponent)
    return sei_amount

def main():
    st.title("SEI Amount Checker")
    address = st.text_input('Enter your SEI address:')
    if address and address.startswith('sei'):
        if st.button("Check Eligibility"):
            response_json = check_eligibility(address)

            if response_json.get('message') == 'Internal server is down':
                st.write('Currently SEI Server is Down, check again later')
            elif response_json.get("eligible"):
                eligibleAmount = response_json.get("eligibleAmount")
                st.write("Eligible Amount (usei):", eligibleAmount)

                number_usei = int(re.search(r'\d+', eligibleAmount).group())
                st.write("Numeric Amount (usei):", number_usei)

                sei = sei_amount(number_usei)
                st.write("Eligible Amount (sei):", sei)
            else:
                st.write("You are not Ahoy.")
    else:
        st.write("Invalid address or network.")

if __name__ == "__main__":
    main()



