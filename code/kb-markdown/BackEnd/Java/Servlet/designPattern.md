## index.jsp

if (log in) redirect to home.jsp
else {
form[post, Home.jsp]
email[email]
password[password]
signin[submit]
signup[submit]
}

## Home.jsp

if (not log in) redirect to index.jsp
else {
email
Create Post link => CreatePost.jsp
Search Post link => Search.jsp
Delete Post link => Delete.jsp
Filter Post link => Filter.jsp
Logout Post link => Logout.jsp
}

## CreatePost.jsp

if (not log in) redirect to index.jsp
else {
email
form[post, ViewPostByID.jsp]
title[text]
tag[text]
description[textarea]
home.jsp link    
}

## Search.jsp

if (not log in) redirect to index.jsp
else {
email
list by email
home.jsp link    
}

## Logout.jsp

Delete session
redirect to index.jsp

## Filter.jsp

if (not log in) redirect to index.jsp
else {
email
dropdown[tags]
list by tag
home.jsp link
}



