SELECT * FROM [CovidDeaths3.0];


--Looking at total cases and deaths for the entire data
SELECT location, date, total_cases, total_deaths
FROM dbo.[CovidDeaths3.0] order by 1,2;


--Looking at Total Cases Vs Total Deaths
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 As DeathPercentage
FROM dbo.[CovidDeaths3.0] 
order by 1,2;



--Getting error for the division column "Death Percentage" this was due to the data type for total_deaths columns being the wrong datatype, changing it to a float 
ALTER TABLE dbo.[CovidDeaths3.0]
ALTER COLUMN total_deaths float;


--Returning Next day, will need to do the "Use" statement in order to use the proper Database
USE [Portfolio Projects]



--Looking at Total Cases vs Totals death in United States to show Likelihood of dying 
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 As DeathPercentage
FROM dbo.[CovidDeaths3.0] 
WHERE Location LIKE '%states%'
order by 1,2;


--Looking at Total Cases vs Population
--Shows what % of population got covid in the United States
SELECT location, date, total_cases, population, (total_cases/population) AS PopulationPercentage
FROM dbo.[CovidDeaths3.0]
WHERE location like '%states%'
order by 1,2;


--Looking at countries with higest infection Rate compared to population
SELECT location, population,  MAX(total_cases) AS HighestInfectionCount, MAX((total_cases/population))*100 AS PopulationPercentageInfected
FROM dbo.[CovidDeaths3.0]
GROUP BY location, population
ORDER by PopulationPercentageInfected desc;



--Showing countries with highest Death count per population
SELECT location, MAX(cast(total_deaths as int)) AS TotalDeathCount
FROM dbo.[CovidDeaths3.0]
WHERE continent is NOT NULL
GROUP BY location
ORDER by TotalDeathCount desc;


--showing Continent with highest death count per population
SELECT continent, MAX(cast(total_deaths as int)) AS TotalDeathCount
FROM [dbo].[CovidDeaths3.0]
--I used this LEN (length) to remove the "world" as a population and only see the other continents
WHERE LEN(continent) > 2
GROUP BY continent
ORDER by TotalDeathCount desc;


--Global Numbers throughout 2020-21

SELECT date, SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) AS Total_deaths, SUM(new_deaths)/nullif(SUM(NEW_CASES),0) *100 as DeathPercentage
FROM dbo.[CovidDeaths3.0]
WHERE continent is not null
GROUP BY date
ORDER BY 1,2;


--Global numbers across the entire world
SELECT  SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) AS Total_deaths, SUM(new_deaths)/nullif(SUM(NEW_CASES),0) *100 as DeathPercentage
FROM dbo.[CovidDeaths3.0]
WHERE continent is not null
ORDER BY 1,2;




--Looking at Total Population vs Vaccination
SELECT d.continent, d.location, d.population, d.date, v.new_vaccinations
FROM [CovidDeaths3.0] d
JOIN [dbo].[CovidVaccinations3] v
	on  d.location = v.location 
	AND
	d.date = v.date
	WHERE LEN(d.continent) > 1
	ORDER BY 2,3;
