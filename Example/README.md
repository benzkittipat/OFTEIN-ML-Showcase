# OFFTEIN++ & IoTCloudserve@TEIN Workshop for IoTFun Class 2020 Term 2

6th April 2021

##### Contact speakers: 

natt.visavarungroj@gmail.com

kittipat.sae@gmail.com



##### Materials: [publish IoTFunClass Slide.pptx - Google Drive](https://drive.google.com/file/d/14Yta0JuNornmt_vbE3AsIzk6_JT3BPzC/view)

##### VDO Part 1 (morning): [iotfun_20210406_iotcloudserve_workshop_part1morning_kubernetes_jupyterworkload.mp4 - Google Drive](https://drive.google.com/file/d/1gts4JFOUXJm9kQVC4vNwaosYGzPNtzCy/view)

##### VDO Part 2 (afternoon): [iotfun_20210406_iotcloudserve_workshop_part2afternoon_persistentvolume_git.mp4 - Google Drive](https://drive.google.com/file/d/1IbTJDLNb8HzR_C_1CJS1c3zYnoPQbki0/view)



## Example .ipynb for OFFTEIN++ & IoTCloudserve@TEIN IoTFun Class 2021 Workshop



<img src="C:\Users\Popo\Pictures\Logo_iotcloudserve.png" style="zoom: 50%;" />

This is the example for IoTFunClass 2021 on 6th Aprill

URL to use IoTCloudServe : iotcloudserve.net

In this example we will use Covid-19 API to study infected people statistics

Covid 19 API : https://covid-api.mmediagroup.fr/v1/

Written by IoTcloudServe@TEIN Admin Team 2021 (Kittipat Saengkaenpetch & Natt Visavarungroj)

```
Contact : natt.visavarungroj@gmail.com
          kittipat.sae@gmail.com

support by https://github.com/IoTcloudServe
           https://github.com/OFTEIN-NET/OFTEIN-MultiTenantPortal
           https://github.com/benzkittipat/OFTEIN-ML-Showcase
```

### 1st Part : Calling Covid-19 API and plot Deaths VS. first 40 days

##### 1.1 Prepare Data 

​	we can call API about the "Deaths Cases" 

##### 	Example : we called deaths cases in Thailand due to Covid-19 in each day 

​	<u>Click Below</u> 

​	<img src="C:\Users\Popo\Pictures\point down.png" style="zoom:40%;" />

​	[](https://covid-api.mmediagroup.fr/v1/history?country=Thailand&status=Deaths)



![](C:\Users\Popo\Pictures\1st_plot.png)

​												<u>Fig.1 Graph Deaths VS. first 40 days (US, Th, Fr, Ind, SKR</u>



Let's make some basic ML :) . In this workshop we used K-mean to classify How well the country tackle the covid-19 epidemics by using Covid-19 API. In your project, you can use any algorithm, Data set you want. 

### 2nd Part : K-Means 

#####  2.1 Prepare Data 

​		call the Raw Data in JSON format 

##### 		Example Raw Data 

​		<img src="C:\Users\Popo\AppData\Roaming\Typora\typora-user-images\image-20210407164652898.png" alt="image-20210407164652898" style="zoom: 67%;" />

using the pandas library , we got the data in panda Dataframe 

<img src="C:\Users\Popo\AppData\Roaming\Typora\typora-user-images\image-20210407182335481.png" alt="image-20210407182335481" style="zoom:50%;" />

##### Next, we will train our algorithm by processing all the data. Here the number of clusters will be 5. This number is given arbitrarily by us. we can choose any number to define the number of clusters

<img src="C:\Users\Popo\AppData\Roaming\Typora\typora-user-images\image-20210407183501372.png" alt="image-20210407183501372" style="zoom: 50%;" />



##### we can see our 5 centers by using the following command

<img src="C:\Users\Popo\AppData\Roaming\Typora\typora-user-images\image-20210411144641511.png" alt="image-20210411144641511" style="zoom: 50%;" />

##### To check the labels created, we can use the following command. It gives the labels created for our data

<img src="C:\Users\Popo\AppData\Roaming\Typora\typora-user-images\image-20210411152247120.png" alt="image-20210411152247120" style="zoom:50%;" />

##### We are going to use the fit predict method that returns for each observation which cluster it belongs to.it will return this cluster numbers into a single vector that is called y K-means

<img src="C:\Users\Popo\AppData\Roaming\Typora\typora-user-images\image-20210411152414718.png" alt="image-20210411152414718" style="zoom:50%;" />

##### plotting the results:

![image-20210411152642147](C:\Users\Popo\AppData\Roaming\Typora\typora-user-images\image-20210411152642147.png)

<img src="C:\Users\Popo\AppData\Roaming\Typora\typora-user-images\image-20210411152725786.png" alt="image-20210411152725786" style="zoom: 45%;" />

### saving output

#### write CSV output file

since data2 is our output file is the panda dataframe, we can use to_csv to convert output to csv.

<img src="C:\Users\Popo\AppData\Roaming\Typora\typora-user-images\image-20210411152857037.png" alt="image-20210411152857037" style="zoom:50%;" />

