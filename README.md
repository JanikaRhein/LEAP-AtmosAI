# LEAP-AtmosAI

**Project Summary:**  
"A Data-Driven Parameterization of Atmospheric Small-Scale Processes"  

by Janika Rhein  

Climate models are essential tools for predicting the effects of human-induced climate change. They
need to provide stable simulations over decades to centuries, which makes achieving very high
spatial resolution computationally impossible. Therefore, they approximate small-scale processes
such as cloud formation, turbulence, and radiation with so-called parameterizations – mathematical
models that capture their average influence on the large-scale atmosphere without explicitly
simulating the processes. However, conventional parameterizations often rely on empirical
relationships or rough assumptions, leading to inaccuracies that accumulate in long-term climate
simulations and limit the forecast quality.  
In this project, which was developed in the Intermediate Machine Learning course at opencampus, I
started developing an AI-supported parameterization for these small-scale atmospheric processes.
This approach allows climate models to be calculated more accurately and efficiently at the same
time – an important step toward enabling more precise climate forecasts with reduced
computational effort. The basis for this work was the dataset from the Kaggle competition "LEAP:
Atmospheric Physics using AI," which comes from high-resolution climate simulations on exascale
supercomputers. The model simulated detailed small-scale processes for each coarse grid cell,
providing an excellent data foundation for ML-based parameterizations. The dataset includes 25
input variables from the coarse model and 14 target variables from the fine-scale models, including
several vertical profiles with 60 altitude levels.  
To determine the relevant input variables for each target variable, I combined climate physics
expertise with correlation analyses. The target variables can be grouped into five categories:

- Temperature (warming trend),  
- Clouds (moisture trend, changes in the amount of liquid cloud droplets and ice crystals),  
- Wind (accelerations in eastward and northward directions),  
- Radiation (shortwave radiation with five components and longwave outgoing radiation),  
- Precipitation (rain and snow rate).  
 
Based on this, I trained seven separate models – initially, a Multi-Layer Perceptron (MLP) for each.
Initial results show that scalar target variables (radiation and precipitation) can already be well
predicted with this simple model. However, more complex architectures are required for the
remaining target variables (temperature, clouds, and wind), which need to capture the spatial
structure of the vertical profiles more effectively.  
This project demonstrates the potential of AI in climate modeling: By using data-driven methods,
physically grounded but computationally expensive processes can be approximated more efficiently,
enabling more accurate and resource-efficient climate simulations. AI-based approaches are
increasingly being used in climate research – from atmospheric physics to ocean modeling.  

Link to the repository: https://github.com/JanikaRhein/LEAP-AtmosAI
