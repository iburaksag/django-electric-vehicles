# Django EV-Database Web Application

I will be quite limited in the types of queries you can run against the database, so you will need to think very carefully about how you structure and store your data to facilitate querying. In this project, the types of queries that can be run against the database were quite limited. The Python Django framework was used to develop the project and the following coding tasks were performed.


## Coding Tasks
### • Group 1 tasks 
1. Application that has a working login/logout service.
2. Datastore object to represent an EV it should have attributes to represent.
– name, manufacturer, year, battery size (Kwh), WLTP range (Km), cost, power (Kw).
3. Seperate page for adding an EV to the database.
4. Add in a form for querying the EV database. it should be able to filter on all attributes.
– Attributes that are string based should have a single input string.
– Attributes that are numerical should specify a range with upper and lower limit (limits included in search).
– This should be accessible regardless of login status.
– Display a list of EVs that satisfy the query as a list of hyperlinks.
– If nothing selected on the form then show full EV list
### • Group 2 tasks 
5. When a hyperlink has been clicked go to a seperate page showing the information of that EV.
6. Add the ability to edit an EV from its information page.
7. Add the ability to delete an EV from its information page.
8. Seperate page for comparing 2 or more EVs.
### • Group 3 tasks
9. On EV comparison page for each attribute highest value should be highlighted green and lowest red. Opposite for cost.
10. On EV comparison page EV names should be hyperlinks to information page.
11. Add in the ability for a logged in user to submit a review of an EV including a text field (limited to 1,000 characters) and a rating out of 10.
12. The reviews should be visible to all users even if logged out
### • Group 4 tasks 
13. On the information page for an EV this should show the average score of all reviews.
14. On the information page for an EV the reviews should be shown in reverse chronological order.
15. On the comparison page for EVs the average score should be added in and highlighted green if highest and red if lowest.
16. UI Design: well thoughout UI design that is intuitive and easy to use.
