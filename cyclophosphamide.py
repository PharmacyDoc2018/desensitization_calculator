class Cyclophosphamide:
    
    def name():
        return "cyclophosphamide"
    
    def concentration():
        return 200
    
    def dilution_num():
        return 2
    
    def dilutions():
        return {
            "step_1": {
                "initial_conc": 20,
                "drug_vol": 1,
                "diluent": "NS",
                "diluent_amount": 9,
                "final_conc": 2
            }
        }
    
    def total_bag_num():
        return 4
    
    def bags():
        return {
            1: {
                "dose_modifier": 0.001, # bag_dose = total_dose * dose_modifier
                "drug_conc_added": 2, # mg/mL
                "dose_volume": lambda dose: (dose * Cyclophosphamide.bags()[1]["dose_modifier"])/ Cyclophosphamide.bags()[1]["drug_conc_added"],
                "diluent_bag": "NS",
                "diluent_bag_size": 250, # mL
                "diluent_bag_total_vol": 275, # mL
                "infusion_time_first_dose": 1, # hour
                "infusion_time_sub_dose": 0.5 # hour
            },
            2: {
                "dose_modifier": 0.01, # bag_dose = total_dose * dose_modifier
                "drug_conc_added": 2, # mg/mL
                "diluent_bag": "NS",
                "diluent_bag_size": 250, # mL
                "diluent_bag_total_vol": 275, # mL
                "infusion_time_first_dose": 1, # hour
                "infusion_time_sub_dose": 0.5 # hour
            },
            3: {
                "dose_modifier": 0.1, # bag_dose = total_dose * dose_modifier
                "drug_conc_added": 20, # mg/mL
                "diluent_bag": "NS",
                "diluent_bag_size": 250, # mL
                "diluent_bag_total_vol": 275, # mL
                "infusion_time_first_dose": 1, # hour
                "infusion_time_sub_dose": 0.5 # hour
            },
            4: {
                "dose_modifier": 0.889, # bag_dose = total_dose * dose_modifier
                "drug_conc_added": 20, #m g/mL
                "diluent_bag": "NS",
                "diluent_bag_size": 250, # mL
                "diluent_bag_total_vol": 275, # mL
                "infusion_time_first_dose": 1, # hour
                "infusion_time_sub_dose": 0.5 # hour
            }
        }