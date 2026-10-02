# Lab 2 decision note — bookstore restock predictions

Complete each prompt in your own words after running your code.

## Classification — reorder category

- Features used: units_sold_last_week, stock_on_hand and days_until_delivery. the target label was reorder_now 
- Label predicted: B001 = YES, B002 = YES, B003 = NO, B004 = YES, B005 = NO 
- Prediction for product B019: YES
- Prediction for product B020: NO
- What should bookstore staff check before acting on these predictions?
Staff should check their current stock amount for each product as well as total units sold last week 
## Regression — suggested quantity

- Numeric estimate for product B019: 40
- Numeric estimate for product B020: 0
- What do these estimates suggest? (Do not call them guaranteed order quantities.)
The estimates suggest a starting point for inventory restocks based off of past data. 

## Limitation and next step

- One limitation of this small fictional dataset or these models: the model operates on a small data set. Only using one variable which is units_sold_last_week. It ignores other variables such as warehouse capacity or time of year. 
- One reasonable next step before using model output in an actual inventory decision: Staff should verify shelf stock and apply that to work with other factors that the data model could not include. Such as local events, or seasonal sales. 
