# map inputs to targets:
input_to_target_mapping = {
    "heating_tend": (
        # Input indices
        [
            list(range(1, 61)),  # temperature[:,1:61]
            list(range(61, 121)),  # humidity[:,61:121]
            list(range(121, 181)),  # liquid clouds mixing ratio [:,121:181]
            list(range(181, 241)),  # ice clouds mixing ratio [:,181:241]
            list(range(377, 437)),  # ozone [:,377:437]
            list(range(437, 497)),  # methane [:,437:497]
            list(range(497, 557)),  # NO2 [:,497:557]
            [362],  # solar insolation [362]
            [364],  # sensible heat flux [364]
            [368],  # albedo [368]
            [372],  # upward LW flux [372]
        ],
        # Flatten the input indices into a single list
        list(range(557,617))  # Target: heating tendency [:,557:617]
    ),
    "moistening_and_clouds": (
        # Input indices
        [
            list(range(61, 121)),  # humidity[:,61:121]
            list(range(121, 181)),  # liquid clouds mixing ratio [:,121:181]
            list(range(181, 241)),  # ice clouds mixing ratio [:,181:241]
        ],
        # Flatten the input indices into a single list
        [
         list(range(629, 677)),  # Target: moistening tendency [:,629:677]
         list(range(689, 737)),  #liquid cloud change [689:737]
         list(range(749, 797))]  # ice cloud change [749:797] 
    ),
    "dudt": (
        # Input indices
        [
            list(range(181, 241)),  # ice clouds mixing ratio [:,181:241]
            list(range(241, 301)), # zonal velocity [:,241:301]
            [365],# zonal windstress [:,365]
            [363]# latent heat flux [:,363]
        ],
        # Flatten the input indices into a single list
        list(range(797, 857))  # Target: zonal acceleration [:,797:857]
    ),
    "dvdt": (
        # Input indices
        [

            list(range(181, 241)),  # ice clouds mixing ratio [:,181:241]
            list(range(301, 361)), # meridional velocity [:,301:361]
            [366]# meridional windstress [:,365] 
        ],
        # Flatten the input indices into a single list
        list(range(857, 917))  # Target: meridional acceleration [:,857:917]
    ),
    "SW_radiation": (
        # Input indices
        [
            list(range(1, 61)),  # temperature[:,1:61]
            [362],  # solar insolation [362]
            [363],  # latent heat flux [:,363]
            [364],  # sensible heat flux [:,364]
            [368],  # albedo [:,368]
            [372],  # upward LW flux [:,372]
        ],
        # Flatten the input indices into a single list
            [917,921,922,923,924]  # Target: NETSW[:,917], direct_solar_visible[:,921], direct_solar_IR[:,922], diff_visible[:,923], diff_IR[:,924] 
    ),
    "FLWDS": (
        # Input indices
        [
            list(range(61, 121)),   # humidity[:,61:121]
            list(range(121, 181)),  # liquid clouds mixing ratio [:,121:181]
            list(range(181, 241)),  # ice clouds mixing ratio [:,181:241]
            list(range(241, 301)),  # zonal velocity [:,241:301]
            list(range(377, 437)),  # ozone [:,377:437]
            list(range(437, 497)),  # methane [:,437:497]
            list(range(497, 557)),  # NO2 [:,497:557]
            [361],                  # surface pressure [:,361]
            [363],                  # latent heat flux [:,363]
            [372],                  # upward LW flux [:,372]
            [373],                  # sea-ice fraction [:,373]
            [375],                  # ocean fraction [:,375]
            [376]                   # snow depth [:,376]
        ],
        # Flatten the input indices into a single list
        [918]  # Target: downward longwave flux at surface [:,918]
    ),
    "snow_and_rain": (
        # Input indices
        [
            list(range(1, 61)),    # temperature[:,1:61]
            list(range(61, 121)),   # humidity[:,61:121]
            list(range(121, 181)),  # liquid clouds mixing ratio [:,121:181]
            list(range(181, 241)),  # ice clouds mixing ratio [:,181:241]
            list(range(241, 301)),  # zonal velocity [:,241:301]
            list(range(377, 437)),  # ozone [:,377:437]
            list(range(437, 497)),  # methane [:,437:497]
            list(range(497, 557)),  # NO2 [:,497:557]
            [372]                   # upward LW flux [:,372]
        ],
        # Flatten the input indices into a single list
        [919,920]  # Target: snow[:,919] and rain [:,920] 
    )
}

# Flatten the nested input and output indices into a single list for each target
def flatten(lst):
    """Flatten list only if it's nested"""
    return [i for sublist in lst for i in sublist] if any(isinstance(i, list) for i in lst) else lst

for target, (inputs, outputs) in input_to_target_mapping.items():
    input_to_target_mapping[target] = (
        flatten(inputs),   # Flatten if needed
        flatten(outputs)  # Flatten if needed
    )
