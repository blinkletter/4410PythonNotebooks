# Exploration of Aspirin Hydrolysis

This *Jupyter* book provides descriptions and access to the *Jupyter* notebooks used to generate the data, derive equations and produce plots associated with the handout for this class. the following notebooks are contained in this book.

## 1: The Literature Equation

This notebook presents the equation used by the authors (note: it's wrong). the equation was assembled as a *SymPy* equation and plotted using the plot tool built-in to *SymPy*.

>**Title**: [1: The Literature Equation](01-Kirby2_PlotEqsFromPaper.ipynb) <br>
>**Tools**: *Python* math operators, *SymPy*  <br>
>**Skills**: Creating, manipulating and plotting math expressions using *SymPy* tools.

## 2: The Correct Equation

The same as above except that the correct equation is used.

>**Title**: [2: The Correct Equation](02-Kirby2_PlotEqsFromPaper.ipynb) <br>
>**Tools**: *SymPy*  <br>
>**Skills**: Creating, manipulating and plotting math expressions using *SymPy* tools.

## 3: Integrating the Rate Laws

In this notebook the equation that predicts the change in absorbance vs time is derived by solving the differential equations of the rate laws.

>**Title**: [3: Integrating the Rate Laws](03-Kirby2_PlotEqsFromPaper.ipynb) <br>
>**Tools**: *SymPy*, *NumPy*, *MatPlotLib*  <br>
>**Skills**: Using *SymPy* tools to perform integration analytically. Calculating values using the derived *SymPy* equation as a function via the `sympy.lamdify()` tool. *NumPy* and *MatPlotLib* are also used.

## 4: Numeric Integration

The numerical integration tools of the *SciPy* package are demonstrated. 

>**Title**: [4: Numeric Integration](04-Kirby2_PlotEqsFromPaper.ipynb) <br>
>**Tools**: *SciPy*, *NumPy*, *MatPlotLib*  <br>
>**Skills**:  Numeric integration using `scipy.integrate.solveivp()`. Again, *NumPy* and *MatPlotLib* are also used to plot the resulting numeric results.

## 5: Abs vs Time Data Analysis

The model for abs vs time that was presented and derived above is used to curve fit the simulated data and find the best-fit values for the parameters. Most of the plots in the exploration document were produced in this notebook and the following notebook.

>**Title**: [5: Abs vs Time Data Analysis](05-Kirby2_DataAnalysis.ipynb) <br>
>**Tools**: *pandas*, *SciPy*, *NumPy*, *MatPlotLib*, *Uncertainties*, *lmfit*  <br>
>**Skills**: Curve fitting using `scipy.optimize.curve_fit()` and `lmfit.model.fit()`. Creating sophisticated and informative plots using *MatPlotLib*. using *uncertainties* to propagate errors and calculate the confidence interval for the curve fit.

## 6: pH-Rate Data Analysis

We derive the model that predicts $k_{obs}$ at a give pH value. Using this model we can curve fit the pH-rate profile to find best-fit parameters for the rate constants that are in the model.

>**Title**: [6: pH-Rate Data Analysis](06-Kirby2_DataAnalysis.ipynb) <br>
>**Tools**: *pandas*, *SciPy*, *NumPy*, *MatPlotLib*, *Uncertainties*, *lmfit*  <br>
>**Skills**: Curve fitting using `lmfit.model.fit()`. Creating informative plots using *MatPlotLib*. using the tools of *lmfit* to calculate the confidence interval for the plot.

## X: Creating Data Sets

Using the equation that predicts abs vs time (the correct one), we can use this notebook to create sets of simulated data. the authors did not provide their raw data so I faked some results to allow us to explore the data analysis methods that may have been used. The data enalayzed using the notebooks above was created using this final notebook.

>**Title**: [X: Creating Data Sets](04X-Kirby2_PlotEqsFromPaper.ipynb) <br>
>**Tools**: *pandas*, *SciPy*, *NumPy*, *MatPlotLib*  <br>
>**Skills**: >**Skills**:  Numeric integration using `scipy.integrate.solveivp()`. Usings *pandas* tools to create a data table and save it as a csv file. 
