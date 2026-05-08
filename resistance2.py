import streamlit as st
def resistance_calculator_series(r1, r2, r3):
   r_total_s = r1+r2+r3
   return r_total_s
def resistance_calculator_parallel(r1, r2, r3):
    if r3 == None:
        return 1/(1/r1+1/r2)
    r_total_p = 1/(1/r1+1/r2+1/r3)
    return r_total_p

st.title("Resistance Calculator")
st.markdown("### Select type")
choice = st.radio("", ["Series", "Parallel"])
if choice == "Series":
         num = st.radio("Number of resistors", [2,3])
         if num == 2:
              r1 = st.number_input("Enter the 1st resistance", min_value=0.0, value=None, placeholder="Enter resistance..", key="b1")
              r2 = st.number_input("Enter the 2nd resistance", min_value=0.0, value=None, placeholder="Enter resistance..", key="b2")
              r3 = None
              if st.button("Calculate"):
                  if r1 is None or r2 is None:
                      st.error("Please fill in the resistance parameters")
                  else:
                      result = resistance_calculator_series(r1, r2, r3)
                      st.success(f"{result:.2f} ohms");
         elif num == 3:
             r1 = st.number_input("Enter the 1st resistance", min_value=0.0, value=None,
                                  placeholder="Enter resistance..", key="s1")
             r2 = st.number_input("Enter the 2nd resistance", min_value=0.0, value=None,
                                  placeholder="Enter resistance..", key="s2")
             r3 = st.number_input("Enter the 3rd resistance", min_value=0.0, value=None,
                                  placeholder="Enter resistance..", key="s3")
             if st.button("Calculate"):
                 if r1 is None or r2 is None or r3 is None:
                     st.error("Please fill in the resistance parameters")
                 else:
                     result = resistance_calculator_series(r1, r2, r3)
                     st.success(f"{result:.2f} ohms");
elif choice == "Parallel":
    num = st.radio("Number of resistors", [2, 3])
    if num == 2:
        r1 = st.number_input("Enter the 1st resistance", min_value=0.0, value=None, placeholder="Enter resistance..",
                             key="a1")
        r2 = st.number_input("Enter the 2nd resistance", min_value=0.0, value=None, placeholder="Enter resistance..",
                             key="a2")
        r3 = None
        if st.button("Calculate"):
            if r1 is None or r2 is None:
                st.error("Please fill in the resistance parameters")
            else:
                result = resistance_calculator_parallel(r1, r2, r3)
                st.success(f"{result:.2f} ohms");
    elif num == 3:
        r1 = st.number_input("Enter the 1st resistance", min_value=0.0, value=None,
                             placeholder="Enter resistance..", key="p1")
        r2 = st.number_input("Enter the 2nd resistance", min_value=0.0, value=None,
                             placeholder="Enter resistance..", key="p2")
        r3 = st.number_input("Enter the 3rd resistance", min_value=0.0, value=None,
                             placeholder="Enter resistance..", key="p3")
        if st.button("Calculate"):
            if r1 is None or r2 is None or r3 is None:
                st.error("Please fill in the resistance parameters")
            else:
                result = resistance_calculator_parallel(r1, r2, r3)
                st.success(f"{result:.2f} ohms");