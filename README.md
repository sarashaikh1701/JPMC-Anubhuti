# Team 32 - Octacore

## Problem Statement - provided by NGO Anubhuti

How can technology help anubhuti collect data/informatiom from Fellows(staff) and analyze it on a daily,
weekly, monthly and quarterly basis to evaluate the program's impact and reach? The organization needs help
in streamlining the data collection and developing data visualizations of their impact to strengthen their pitches to different funders

This project has been implemented as part of JPMC's 24h Code For Good Hackathon '22.

## Solution

We have built a web portal to increase the transparency among fellows and provide visibility to higher authorities. 
To bring uniformity in the data collection process, we have designed a standard form to be filled monthly by every fellow .
The data collected will help in analyzing the trends and deriving meaningful insights to help the organization

## Team Members

  * Saileshwar Karthik
  * Ishika Chokshi
  * Yashwanth CM
  * Dishita Ashar
  * Sara Shaikh
  * Anandi Jindal
  * Mokshesh Vora
  * Shaikh Javeed Suhail 

## Steps to get started

### Pre-requisites

```
pip install virtualenv
virtualenv venv
source virtualenv_name/bin/activate
python requirements.txt
cd reactclient
npm install
```

### Getting backend server running

```
// enter octacore directory
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Getting react web-page running

```
// enter reactclient directory
npm start
```
