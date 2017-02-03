This is my first, crude attempt at making a simple, useful package to calculate the "correction factor" (terminology from Plume et al. 2012 and Goldsmith et al. 1997) when estimating column densities.

The core of it will be a function named, more or less, `correction_factor` which takes as inputs the

The backend will really just be making RADEX calls and then doing some simple math on them.
I'll probably need to think carefully and usefully about how I will handle different molecules.

I anticipate using the `pyradex` package for the serious calculations.

I'll try to make it python3 compatible.