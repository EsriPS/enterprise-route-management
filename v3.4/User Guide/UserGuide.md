# Enterprise Route Management Read Me
Enterprise Route Management (ERM) is an optimization pattern provided by Esri which leverages a combination of off the shelf tools from the Esri stack, a user facing interface for exposure that does not require the user to be familiar with GIS, and a number of back-end tools to communicate between the various tools and systems.
## Key Terms
- Routes - these represent the mobile resources who do work. This can be just an employee or in cases of capacitated problems (e.g. a truck driver who drives a truck that has a maximum capacity)
- Orders - these represent the work that needs to be done, like a work order, service order, pickup or delivery
- Dispatch Location - the office location for which the user is planning for
- Depots - the start and/or ending location of routes
- Zones - optional geographic zones that may be used to confine routes to a specific area
- Plan - the dispatch location, date and time combination that will be used to request the related orders, routes and depots to be used in the optimization 
- Vehicle Routing Problem (VRP) - the service that optimally distributes the orders across the routes while considering the constraints applied
- Travel Mode - the set of road rules that apply to the routes in the plan
- Assignment rule - This is applied to orders and routes and determines how the VRP treats them
    - Orders
        - Override - the solver will override its current status and place it on the best route
        - Exclude - the solver will ignore this orders
        - Preserve Route and Relative Sequence - keep the order on the assigned route and keep its sequence in the same relative spot to the other assigned orders
        - Anchor First - force this order to be the first stop on a route
        - Anchor Last - force this order to be the last stop on a route
    - Routes
        - Include - optimize this route
        - Exclude - do not optimize this route
## Logging Into the App
Users sign in with the Portal named user. Users are part of Portal groups which dictate which dispatch locations users are authorized to plan for.
## Creating a New Plan
The most common workflow for users is starting a new plan for the current day. This is achieved by clicking on the "Create New Plan" button. Users then select the dispatch location they want to plan for from the drop down, select a date and time they want to plan for. The definition of the time and day may differ based on customer business systems but it generally represents the cutoff time window for any orders that need to be included in the plan.
## Open a Prior Plan
In some cases, a user may want to revisit a plan they, or someone else in their planning location, already started. To do so, users can click on "View Plan" next to any plan shown on the first screen displayed when the user logs in.
## Parts of a Plan

### Collections
Collections are a way of grouping orders that make it easy to remove orders from a plan. Commonly, they represent things like trailers or stores full of orders, and by unchecking a collection and updating, all the orders in that collection are excluded and effectively removed from the plan until the collection is added back to the plan.
### Orders
Orders represent the work that needs to be done and have a variety of attributes on them. While some attributes are purely contextual information for the users, some constrain the routing problem. Some examples of these are time windows (what are the upper and lower bounds of time that an order can be serviced), specialty (are there only certain types of routes that can service this order), capacity (weight, length, pallet count, etc.). Administrators control which attributes are visible and/or editable.
### Routes
Routes are the mobile resources that can service orders. Like orders, they have some attributes that are contextual and others that constrain the optimization problem. Some examples of constraining attributes are start time, capacity, specialty, max total time, and max total distance. The VRP considers the constraints of the orders, the constraints of the routes and the cost settings on the routes and tries to solve the problem by servicing the most amount of orders it can in the lowest cost fashion. Also, like orders, administrators control which attributes are visible and/or editable.
## Optimizing a Plan
By default, users may click on "Optimize Plan" to run the VRP against all orders and routes to determine the best distribution of orders across routes. Alternatively, they can also:
- Select only a limited number of routes and optimize only those routes
- Select only a limited number of routes to re-sequence those routes only
- Select only a limited number of routes and validate their current assignments do not violate any constraints

Administrators control which optimization modes are available. After running a route or routes through the VRP, solved routes will show their status tag change from "Unsolved" to "Solved."
## Manually Modifying a Plan
Outside of optimization, routes and orders can have manual assignment. An unassigned order or orders can be selected, users can then click on "Assign Orders" and select the desired route to put it on. The same can be done to orders assigned to a route in order to put them on another route. Users can also drag an order up or down in a route to change its sequence. All routes must be sent back to the solver to validate any manual assignments.
## Refreshing a Plan
At any time, a user my click on the "Refresh Plan" button. This makes a request to the business system to load any new orders into the plan as well as any attribute changes for orders that are already in the plan. It may remove orders from a plan that should no longer be included. The same applies to collections. 
## Creating a Dashboard
At any time, a user may click on "Create Dashboard." This creates a report dashboard in the format that the administrator has defined for the organization. After the dashboard is created, the user may click on "Open Dashboard" to view the dashboard for that plan.
## Committing Routes
Users may click "Commit Routes" to commit all routes or select a subset set of routes to commit. The commit action sends a message to the business system on which routes are done being planned so that it may retrieve any required information need to update the business system. If using Esri mobile apps, this also triggers the synchronization of the plan to those apps.