# Explore US Bikeshare Data

In this project, you will use data provided by [Motivate](https://www.motivateco.com), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

This app compute variety of descriptive statistics. it will provide the following information:

1 Popular times of travel (i.e., occurs most often in the start time)

[] most common month
[] most common day of week
[] most common hour of day

2 Popular stations and trip

[] most common start station
[] most common end station
[] most common trip from start to end (i.e., most frequent combination of start station and end station)

3 Trip duration
[] total travel time
[] average travel time

4 User info
[] counts of each user type
[] counts of each gender (only available for NYC and Chicago)
[] earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Getting started
## Create a Conda virtual environment:
```
conda create --name bikeshare python=3.8
```

## Activate the virtual environment:
```
conda activate bikeshare
```

## Clone the repository:

In the virtual environment created in the previous step, type the following commands
```
git clone https://gitlab.com/fmsaibi/explore-us-bikeshare-data.git
cd explore-us-bikeshare-data
```

## Install dependencies:
In the virtual environment created in the previous step, type the following commands
```
conda install --file requirements.txt
```
## Usage

Run the application::
```
python bikeshare.py
```