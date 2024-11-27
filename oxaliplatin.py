class Oxaliplatin:
    
    def name():
        return "oxaliplatin"
    
    def concentration():
        return 5 
    
    def units():
        return "mg"

    def dilution_num():
        return 1 
    
    def dilutions():
        return {
            1: {
                "initial_conc": 5,
                "drug_vol": 1,
                "diluent": "D5W",
                "diluent_amount": 4,
                "final_conc": 1 
            }
        }
    
    def total_bag_num():
        return 4
    
    def bags():
        return {
            1: {
                "dose_modifier": 0.001, # bag_dose = total_dose * dose_modifier
                "drug_conc_added": 1, # mg/mL
                "diluent_bag": "D5W",
                "diluent_bag_size": 100, # mL
                "diluent_bag_total_vol": 110, # mL
                "infusion_time_first_dose": 1, # hour
                "infusion_time_sub_dose": 1 # hour
            },
            2: {
                "dose_modifier": 0.01, # bag_dose = total_dose * dose_modifier
                "drug_conc_added": 1, # mg/mL
                "diluent_bag": "D5W",
                "diluent_bag_size": 100, # mL
                "diluent_bag_total_vol": 110, # mL
                "infusion_time_first_dose": 1, # hour
                "infusion_time_sub_dose": 1 # hour
            },
            3: {
                "dose_modifier": 0.1, # bag_dose = total_dose * dose_modifier
                "drug_conc_added": 5, # mg/mL
                "diluent_bag": "D5W",
                "diluent_bag_size": 100, # mL
                "diluent_bag_total_vol": 110, # mL
                "infusion_time_first_dose": 1, # hour
                "infusion_time_sub_dose": 1 # hour
            },
            4: {
                "dose_modifier": 0.889, # bag_dose = total_dose * dose_modifier
                "drug_conc_added": 5, #mg/mL
                "diluent_bag": "D5W",
                "diluent_bag_size": 250, # mL
                "diluent_bag_total_vol": 275, # mL
                "infusion_time_first_dose": 2, # hour
                "infusion_time_sub_dose": 2 # hour
            }
        }