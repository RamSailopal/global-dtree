# global-dtree

This repo demonstrates the ability to view M (YottaDB/Intersystems/GTm) based globals using d3 dTree

![Alt text](global-dtree.webp?raw=true "Global dTree")

The following CARS global is used for the demonstation:

     ^CARS("Audi","A3","White","Petrol",2020)="$12,450"
     ^CARS("Audi","A8","Grey","Petrol",2016)="$13,200"
     ^CARS("Audi","Q7","Grey","Diesel",2021)="$22,450"
     ^CARS("BMW",320,"Grey","Petrol",2016)="$10,200"
     ^CARS("BMW",330,"Blue","Petrol",2021)="$18,000"
     ^CARS("Land Rover","Evoque","Gold","Diesel",2021)="$43,000"
     ^CARS("Mercedes","GLB","Black","Diesel",2020)="$21,500"
     ^CARS("Mercedes","GLB","Black","Petrol",2020)="$20,050"
     ^CARS("Mercedes","GLC","Red","Petrol",2021)="$21,200"
     ^CARS("Nissan","Civic","Red","Diesel",2019)="$11,000"
     ^CARS("Nissan","Civic","Red","Diesel",2020)="$12,000"
     ^CARS("Nissan","Civic","Red","Petrol",2020)="$11,600"
     ^CARS("Nissan","Qashqai","Blue","Diesel",2018)="$12,400"
     ^CARS("Nissan","Qashqai","Green","Hybrid",2020)="$18,000"
     ^CARS("Toyota","Rav4","Black","Petrol",2019)="$11,400"
     ^CARS("Toyota","Rav4","Green","Petrol",2019)="$11,000"
     ^CARS("Toyota","Rav4","Orange","Petrol",2019)="$11,000"
     ^CARS("Toyota","Rav4","Silver","Petrol",2019)="$11,250"


# Gitpod

To run a Gitpod with this repo:

1) Create a free/paid Gitpod account - https://www.gitpod.io/
2) Log into the account
3) Open a new browser tab and add **gitpod.io/#https://github.com/RamSailopal/global-dtree** to the address - This will create a new Gitpod cloud instance.
4) Wait till there are the Docker compose messages stop scrolling and then click on the ports in the bottom right of the Gitpod window and then the globe icon next to the 8--3 port. This will open another browser tab.
5) Enter CARS for the global and the dTree chart for the global will appear.

