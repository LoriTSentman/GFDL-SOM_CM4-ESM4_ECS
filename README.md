**Overview**        
This repository is home to source code for slab ocean model (GFDL-SOM) configurations of GFDL-CM4 and GFDL-ESM4, input and output datasets, and Jupyter notebook to create analysis figures supporting Sentman et al. (2025), "Quantifying Equilibrium Climate Sensitivity to Atmospheric Chemistry and Composition Representations in GFDL-CM4.0 and GFDL-ESM4.1
".
               
**Motivation**                
The goal of this project is to provide underlying data and code needed to understand, evaluate, and build upon the reported research by Sentman et al. (2025).
                   
**How this repository is structured**    
>`|-- analysisScript`
> Jupyter notebook to produce manuscript and supporting information figures             
`|-- inputData`
> Model input datasets                 
`|-- outputData`
> Output data from experiments in the manuscript                            
`|-- runScripts/`
> C-shell scripts configured for each experiment in the manuscript            
`|-- srcCode`
> Source code for GFDL-SOM_CM4 and GFDL-SOM_ESM4 models used in this study           
                
`|-- analysisScript`           
`|   |-- mathutil.py`                                   
`|   |-- SentmanEtAl2025Figures.ipynb`              
`|   |-- util.py`                                
`|-- inputData`                                 
`|   |-- GFDL-SOM_CM4/`                                 
`|   |-- GFDL-SOM_ESM4/`                                
`|-- outputData`                                  
`|   |-- atmos.static.nc`                
`|   |-- GFDL-CM4_piControl`                   
`|   |   |-- atmos.0061-0080.t_ref.nc`                
`|   |-- GFDL-ESM4_piControl`                   
`|   |   |-- atmos.0061-0080.t_ref.nc`                
`|   |-- GFDL-SOM_CM4_abrupt-2xCO2`               
`|   |   |-- atmos.0001-0100.t_ref.nc`                       
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`             
`|   |-- GFDL-SOM_CM4_piControl`              
`|   |   |-- atmos.0001-0100.t_ref.nc`                    
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`             
`|   |-- GFDL-SOM_ESM4p1_abrupt-2xCO2`          
`|   |   |-- atmos.0001-0100.t_ref.nc`                  
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`             
`|   |-- GFDL-SOM_ESM4p1+CM4bvoc_abrupt-2xCO2`            
`|   |   |-- atmos.0001-0100.t_ref.nc`                     
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`              
`|   |-- GFDL-SOM_ESM4p1+CM4bvoc_piControl`              
`|   |   |-- atmos.0001-0100.t_ref.nc`                        
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`               
`|   |-- GFDL-SOM_ESM4p1+CM4combined_abrupt-2xCO2`          
`|   |   |-- atmos.0001-0100.t_ref.nc`            
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`            
`|   |-- GFDL-SOM_ESM4p1+CM4combined_piControl`          
`|   |   |-- atmos.0001-0100.t_ref.nc`           
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`            
`|   |-- GFDL-SOM_ESM4p1+CM4dust_abrupt-2xCO2`           
`|   |   |-- atmos.0001-0100.t_ref.nc`           
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`             
`|   |-- GFDL-SOM_ESM4p1+CM4dust_piControl`              
`|   |   |-- atmos.0001-0100.t_ref.nc`               
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`            
`|   |-- GFDL-SOM_ESM4p1+CM4noicemask_abrupt-2xCO2`              
`|   |   |-- atmos.0001-0100.t_ref.nc`               
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`              
`|   |-- GFDL-SOM_ESM4p1+CM4noicemask_piControl`                  
`|   |   |-- atmos.0001-0100.t_ref.nc`              
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`              
`|   |-- GFDL-SOM_ESM4p1+CM4o3_abrupt-2xCO2`               
`|   |   |-- atmos.0001-0100.t_ref.nc`           
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`                
`|   |-- GFDL-SOM_ESM4p1+CM4o3_piControl`                
`|   |   |-- atmos.0001-0100.t_ref.nc`             
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`                 
`|   |-- GFDL-SOM_ESM4p1+CM4seasalt_abrupt-2xCO2`                  
`|   |   |-- atmos.0001-0100.t_ref.nc`             
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`             
`|   |-- GFDL-SOM_ESM4p1+CM4seasalt_piControl`                 
`|   |   |-- atmos.0001-0100.t_ref.nc`           
`|   |   |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`             
`|   |-- GFDL-SOM_ESM4p1_piControl`                
`|       |-- atmos.0001-0100.t_ref.nc`                
`|       |-- atmos_month_aer.0001-0100.aer_ex_c_vs.nc`           
`|-- runScripts/`               
`|   |-- GFDL-SOM_CM4_abrupt-2xCO2`               
`|   |-- GFDL-SOM_CM4_piControl`              
`|   |-- GFDL-SOM_ESM4p1_abrupt-2xCO2`               
`|   |-- GFDL-SOM_ESM4p1+CM4bvoc_abrupt-2xCO2`              
`|   |-- GFDL-SOM_ESM4p1+CM4bvoc_piControl`            
`|   |-- GFDL-SOM_ESM4p1+CM4combined_abrupt-2xCO2`             
`|   |-- GFDL-SOM_ESM4p1+CM4combined_piControl`            
`|   |-- GFDL-SOM_ESM4p1+CM4dust_abrupt-2xCO2`           
`|   |-- GFDL-SOM_ESM4p1+CM4dust_piControl`               
`|   |-- GFDL-SOM_ESM4p1+CM4noicemask_abrupt-2xCO2`          
`|   |-- GFDL-SOM_ESM4p1+CM4noicemask_piControl`           
`|   |-- GFDL-SOM_ESM4p1+CM4o3_abrupt-2xCO2`       
`|   |-- GFDL-SOM_ESM4p1+CM4o3_piControl`              
`|   |-- GFDL-SOM_ESM4p1+CM4seasalt_abrupt-2xCO2`            
`|   |-- GFDL-SOM_ESM4p1+CM4seasalt_piControl`           
`|   |-- GFDL-SOM_ESM4p1_piControl`            
`|-- srcCode`           
`    |-- GFDL-SOM_CM4`         
`    |   |-- exec/`     
`    |   |-- src/`         
`    |-- GFDL-SOM_ESM4`          
`    |   |-- exec/`          
`    |   |-- src/`          
`    |-- utilities`        
`        |-- adjust_dry_mass.csh`          
`        |-- combine-ncc`             
`        |-- expand_variables`              
`        |-- mppnccombine`             
`        |-- output.stager`               
`        |-- prepare_dir.csh`             
`        |-- time_stamp.csh`               
`|-- README`                   
