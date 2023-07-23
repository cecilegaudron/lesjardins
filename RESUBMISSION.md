# Les Jardins - RESUBMISSION  
As expected, I had to resubmit my project because it didn't meet the criteria. This resubmission was beneficial for me because I was able to work on my project again without too much stress, and some things that weren't clear finally made sense to me. 
I've made a few changes that provide a better user experience.  

## Table of Content  
-  [Database](#database)  
-  [Changes and Additions](#changes-and-additions)  
-  [Development](#development)  
-  [Testing](#testing)  
-  [Technologies and Credits](#technologies-and-credits)  


## Database  
In order to meet the passage criteria, I had to create new custom models. I decided to create a survey and a wish list.  

![DATABASE](/media/resubmission/diagrame-database.jpg)  

## Changes and Additions  

![TREE STRUCTURE](/media/resubmission/tree-structure.jpg)  

### Layout  
I had to modify the layout of the site a little because it was too close to the "My boutique Ado" tutorial. I changed some styles because not all buttons were similar on the different pages of the site.  
I encountered problems with some styles because there was a conflict between the base.css and header.css files. I had to change some selectors so that the styles in header.css were not applied instead of base.css.  

![MOCKUP MOBILE](/media/resubmission/mobile-mockups.jpg)  

![MOCKUP MOBILE](/media/resubmission/mobile-mockups2.jpg)  

![MOCKUP MOBILE](/media/resubmission/mobile-mockups3.jpg)  

![MOCKUP DESK](/media/resubmission/desk-mockups.jpg)  

![MOCKUP DESK](/media/resubmission/desk-mockups2.jpg)  

### Header and Navbar  
I wasn't satisfied with the previous nav bar. It had display problems and wasn't always user friendly. I'm not a big fan of dropdown menus, which I find unsuitable for small screens. So I decided to divide the header into three parts. The menu is presented in the same way on different screen sizes.  
__The logo at the top__  
__A first menu in a navbar__  
The menu has a sticky property, which is fixed at the top of the page when the user scrolls. This navbar is made up of four elements. A bars icon that opens a collapse menu, a link to the page listing all products, an icon representing the customer account that opens the profile page, specific to each user, and finally the shopping bag icon with the amount to be paid if products are present in the basket.  
__A collapse menu__  
It is presenting the different product categories, an account arear and a contact page.  
In the account area, the different pages accessible to the user, depending on whether or not he's logged in to his account:
- Profile  
- Orders  
- Wishlist  
- Log out  

If the connected user is the admin user, the page for managing the product is displaying. If the user is not connected to his account, the menu shows only register and login pages.  

![MENU CLOSE](/media/resubmission/menu-close.png)  

![MENU OPEN](/media/resubmission/menu-open.png)  

[Go back to the Table of content](#table-of-content)  

### Survey  
I create a new app called "Survey".  
A survey that users can answer, without needing to be logged into their customer account. The main aim is to gather information that will help us to get to know the customers better. Survey results are available in the Admin Panel.  

![SURVEY](/media/resubmission/survey.png)  

[Go back to the Table of content](#table-of-content)  

### Contact  
In the initial project, a contact form was already present, but it wasn't fully operational.  
A number of things weren't quite right and have now been corrected:  
- I don't want the date on which the message was sent to be displayed in the admin panel, as this information is not of interest. I only want to see the date.  
- I've added a max_length to the text area for a better UX.  
- Integration of the app in the Admin Panel. The admin can now view all messages sent via the contact form by connecting to the Admin Panel.  
Fixed bugs such as incorrect url and template name.  
When the email is successfully sent, the user is taken to a page where this information is notified.  

![CONTACT](/media/resubmission/admin-contact.png)  

[Go back to the Table of content](#table-of-content)  

### Wishlist  
I wanted to offer a wishlist. Once logged into their customer account, users can add or remove products from the wishlist. There's also a page where you can consult the list of your favorite products. This enables them to quickly access their favorite products for their next order.  

![PRODUCT](/media/resubmission/product.png)  

![PRODUCT DETAIL](/media/resubmission/product-detail.png)  

On the product list page, as well as on each product page, users can directly add the product to their wishlist by clicking on the heart button.

![WISHLIST](/media/resubmission/wishlist.png)  

I wanted the user to be able to see at a glance whether the product was already featured in his wishslit (by showing a full heart if the product is liked and an empty heart if it isn't). But I can't, I've tried a lot but I just can't get it to work. 

![ADD OR REMOVE TO WISHLIST](/media/resubmission/like-dislike.png)  

However, the app works correctly, the user is notified by a message of the success of the addition and deletion of the product from the wishlist.  
Furthermore, I encounter a display problem when one or more products are present in the shopping bag and a product is added to or deleted from the wishlist. The message informing the user is displayed at the same time as the shopping bag.  

![WISHLIST](/media/resubmission/wishlist-display-pb.png)  

Finally, I'd like to be able to count the number of likes on a product and display it in the admin panel.  

![WISHLIST](/media/resubmission/admin-wishlist.png)  


[Go back to the Table of content](#table-of-content)  

### Other changes and additions  
__Profile pages__  
I've changed the layout of the profile page. It now displays only the personal information that can be added or modified via the form. The email address cannot be modified. Orders placed are now presented on a separate page. This makes them easier to read for the user.

![PROFILE](/media/resubmission/profile.png)  

![ORDER](/media/resubmission/order.png)  

__Breadcrumb__  
I've added a breadcrumb to the products and product details pages. This makes the user's browsing experience much clearer and more readable.  Some categories, such as vegetables, are made up of several categories (vegetables and herbs). With the breadcrumb, the user can display only the "herbs" sub-category.  
However, I can't select only the Herbs category when I'm in Vegetables&Herbs. The two categories are displayed separately but cannot be selected separately.  

__Newsletter__  
I wanted to keep the newsletter subscription only on the home page and not display it on every page. However, I'm having trouble understanding how to link my newsletter app with the Mailchimp module. As a result, the newsletter is present in the admin panel, but subscriptions are not displayed because there is no connection with Mailchimp. Subscriptions and newsletters are sent via the Mailchimp interface.  

__Home Page__  
I've changed the layout of some elements on the home page, to add content for the survey and improve readability.  

__Footer__  
Finally, I changed some styles for footer because the legibility wasn't always up to scratch and the container was much too big.  

### Development 
content  


[Go back to the Table of content](#table-of-content)  

### Lighthouse  
Unfortunately, I don't score well with Lightouse, especially in "performance". I was unable to improve this score in the time available.  

![LIGHTHOUSE MOBILE](/media/resubmission/lighthouse-mobile.png)  

![LIGHTHOUSE DESK](/media/resubmission/lighthouse-desk.png)  

### Features Left to Implement  
- Link shopping list with order
- non modifiable country order to just display FR

## Manual Testing  
content


## Unfixed Bugs  
content 


[Go back to the Table of content](#table-of-content)  

## Technologies and credits
- [Django Multiselectfield](https://pypi.org/project/django-multiselectfield/), to display multiple selections 
- [Gitpod](hhttps://www.gitpod.io/), IDE for building the project  

### Credits  
- [GitHub](https://github.com/), service to store the project  
- [Gitpod](hhttps://www.gitpod.io/), IDE for building the project  