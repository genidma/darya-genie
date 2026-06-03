# Darya Safety-First Certification Assessment

**Total Questions:** 15  
**Passing Score:** 80% (12/15 correct)  
**Time Limit:** 30 minutes

## Quiz Format

Each question is multiple choice. Select the best answer.

---

### Questions

**1.** What is the maximum safe pH level before requiring additional PPE?
- A) 8.5
- B) 9.0
- C) 10.0
- D) Any pH outside 6.5-8.5 requires additional protection

**2.** How often must P100 respirator fit-checks be performed?
- A) Weekly
- B) Before each shift
- C) Daily
- D) Monthly

**3.** What signal indicates immediate evacuation?
- A) Three short whistle blasts
- B) Continuous siren for 30 seconds
- C) One long whistle blast
- D) Radio call "EVAC"

**4.** What is the maximum safe water depth for UGV operations?
- A) 20 cm
- B) 40 cm
- C) 60 cm
- D) 80 cm

**5.** At what battery percentage must drones initiate RTH?
- A) 20%
- B) 25%
- C) 30%
- D) 50%

**6.** How long should motors cool before shutdown?
- A) 10 seconds
- B) 30 seconds
- C) 1 minute
- D) 5 minutes

**7.** What temperature anomaly (from ambient) indicates chemical seepage?
- A) >2°C
- B) >5°C
- C) >10°C
- D) >15°C

**8.** In what order should PPE be removed?
- A) respirator → coveralls → gloves → boots
- B) coveralls → gloves → respirator → boots
- C) gloves → boots → coveralls → respirator
- D) boots → gloves → coveralls → respirator

**9.** What is the minimum VOC reading that requires respirator upgrade?
- A) 100ppm
- B) 250ppm
- C) 500ppm
- D) 1000ppm

**10.** What is the maximum operational slope for UGV?
- A) 10°
- B) 15°
- C) 20°
- D) 25°

**11.** At what wind speed must drone operations cease?
- A) 10 km/h
- B) 15 km/h
- C) 20 km/h
- D) 25 km/h

**12.** What is the safe E. coli count limit in water?
- A) <1000 CFU/mL
- B) <500 CFU/mL
- C) <100 CFU/mL
- D) <50 CFU/mL

**13.** What does purple water discoloration indicate?
- A) Agricultural runoff
- B) Petroleum contamination
- C) Heavy metal presence
- D) Safe for operations

**14.** What is the minimum number of satellites for GPS lock?
- A) 4
- B) 6
- C) 8
- D) 10

**15.** What should you do immediately after equipment rinse at the hub?
- A) Remove PPE
- B) Log operational hours
- C) Begin drying procedures
- D) Get guardian sign-off on cleanliness

---

## Scoring & Certification

Submit your answers via the certification portal. The `certification_gatekeeper.py` script will:
1. Validate all answers against the answer key
2. Generate a certification token upon passing
3. POST to `/api/certify` with user wallet and token
4. Return success/failure response

**Correct Answers:** 1-D, 2-C, 3-B, 4-B, 5-C, 6-B, 7-B, 8-C, 9-C, 10-B, 11-B, 12-C, 13-C, 14-C, 15-D