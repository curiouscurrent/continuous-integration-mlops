"""Power Calculator app using Streamlit."""

import streamlit as st


def main():
    """Run the Streamlit app."""

    # Title and description
    st.title("Power Calculator")
    st.write("Enter a number to calculate its square, cube, and fifth power.")

    # User input
    number = st.number_input("Enter an integer", value=1, step=1)

    # Calculations
    square = number**2
    cube = number**3
    fifth_power = number**5

    # Output results
    st.write(f"The square of {number} is: {square}")
    st.write(f"The cube of {number} is: {cube}")
    st.write(f"The fifth power of {number} is: {fifth_power}")


if __name__ == "__main__":
    main()