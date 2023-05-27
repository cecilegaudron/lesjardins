# Testing  
## Validator Testing  
- HTML  
Many errors are mentioned in the [W3C validator](https://validator.w3.org/nu/). These are errors in my responsive navbar. Unfortunately, I haven't had the time to rework this navbar from scratch in order to correct the erroneous code.  

- CSS  
No errors were found when passing through the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/)  

- JavaScript  
I didn't write my own Javascript code, so I don't need to check it.  

- Python  
My IDE has a built-in python code checker, so I do the checks as I went along. Some lines are too long, but I chose not to cut them in order to keep a better visibility.  

## Lighthouse  
Unfortunately, I don't score well with Lightouse, especially in "performance". I was unable to improve this score in the time available.  

![LIGHTHOUSE MOBILE](/media/screenshots/lighthouse-mobile.png)  

![LIGHTHOUSE DESK](/media/screenshots/lighthouse-desk.png)  

## Manual Testing  

| Problems | Actions | Results |
| ----------- | ----------- | ----------- | 
| Page not found (404). All the website is down when I deleted some products from the dabatase when I am logged with the admin account | I reset the database, delete the migrations files and the pycache folder. I migrate and load again categories and products |  Everything is now fine |
| Error "DETAIL: A field with precision 3, scale 2 must round to an absolute value less than 10^1." | Max_digits was 3 and decimal_places was 2. Max_digits need to be superior than the addition of numbers before and after the comma. So add value 6 for max_digits |  Problem solved with the help of this [article](https://stackoverflow.com/questions/7340215/postgresql-how-to-resolve-numeric-field-overflow-problem) |
| Internal Server Error when site deployed | Turn on debug settings to know the problem : ModuleNotFoundError at / No module named 'stripe'. I install again Stripe and freeze |  Problem solved [commit](https://github.com/cecilegaudron/lesjardins/commit/19e1c607b2b8c4d13b91888eb4d1aef3199558f6) |

### Responsive front-end  
-__Menu__    
The menu is responsive regardless of screen width. But I have a problem with a display bug on large device. 

![TESTING SMALL DEVICES MENU](/media/screenshots/testing-sd-menu.png)  

![TESTING LARGE DEVICES MENU](/media/screenshots/testing-xl-menu.png)  

-__Products Display__  
List of products are displayed correctly regardless of screen width.  

![TESTING SMALL DEVICES PRODUCTS](/media/screenshots/testing-sd-products.png)  

![TESTING MEDIUM DEVICES PRODUCTS](/media/screenshots/testing-md-products.png)  

![TESTING LARGE DEVICES PRODUCTS](/media/screenshots/testing-xl-products.png)  

-__Product Details Display__  
Product details are displayed correctly regardless of screen width.  

![TESTING SMALL DEVICES PRODUCT DETAILS](/media/screenshots/testing-sd-product-details.png)  

![TESTING LARGE DEVICES PRODUCT DETAILS](/media/screenshots/testing-xl-product-details.png)  

### Functionalities  
-__Shopping Bag__  
![TESTING SHOPPING BAG](/media/screenshots/testing-shopping-bag.png)  

![TESTING UPDATE SHOPPING BAG](/media/screenshots/testing-update-bag.png)  

![TESTING REMOVE AN ITEM](/media/screenshots/testing-remove-item-bag.png)  

-__Order__
The order is going well. The success message is displayed to inform the customer that the order has been confirmed. However, the confirmation email is not sent to the user's address.  

![TESTING ORDER](/media/screenshots/testing-order.png)  

-__Online Payment__  
The payment is successfully processed by Stripe. The success message is displaying.  

![TESTING STRIPE PAYMENT](/media/screenshots/testing-paiement-stripe.png)  

-__Newsletter Subscription__
The newsletter subscription has been successfully processed by Mailchimp. The success message is displaying. The new contact is added to the contact list. 

![TESTING MAILCHIMP](/media/screenshots/testing-maichimp.png)  

## Unfixed Bugs  
I have a lot of unfixed bugs, I can't fix them because I haven't had the time to do it correctly. I am so sorry about that and I am sad to submit a project with bugs.  

- I'm also having a problem with the user account and shopping bag part of the menu with the desk screen. When clicking to log in, the menu is displayed horizontally. 

- The most incomprehensible bug is the error : [Errno 101] Network is unreachable  
I want to confirm the admin account from the front end because I had to reset my database a few days ago and I can't confirm it even though the account is active and accessible via the admin panel.  I don't understand why.  

![UNFIXED BUG](/media/screenshots/unfixed-bug.png)  
