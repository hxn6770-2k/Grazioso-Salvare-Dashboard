## Grazioso Salvare Dashboard

## 🐾 About the Project

The **Grazioso Salvare Dashboard** is an interactive web application built to support **Grazioso Salvare**, a search-and-rescue organization operating in Austin, Texas. It streamlines the process of identifying and classifying potential rescue dogs from local animal shelters using filters, data tables, and data visualizations.

---

## ✅ Core Functionality

* **Interactive Filtering:**
  Filter dogs by rescue mission types:

  * Water Rescue
  * Mountain/Wilderness Rescue
  * Disaster/Individual Tracking
    Includes a reset option for clearing all filters.

* **Responsive Data Table:**
  Real-time data updates based on selected filters. Supports efficient data exploration.

* **Data Visualizations:**

  * **Pie Chart**: Shows breed distribution filtered by mission type.
  * **Geolocation Map**: Updates dynamically based on the selected entry in the data table.

---

## 🛠 Tools & Technologies

### 1. **MongoDB**

* NoSQL document database used for storing animal shelter data.
* Chosen for its flexibility in handling unstructured or semi-structured data.
* Integrated with Python using **PyMongo**.

### 2. **Python CRUD Module – `AnimalShelter`**

* Encapsulates **Create, Read, Update, Delete** operations.
* Abstracts database interactions for maintainability and reuse.
* Streamlines dashboard connectivity with MongoDB.

### 3. **Dash (by Plotly)**

* Python framework for building interactive web applications without HTML/JS.
* Components used:

  * `dash_core_components` (`dcc`)
  * `dash_html_components` (`html`)
  * `dash_table.DataTable`
* Integrated with Pandas and Plotly for data manipulation and visualization.
* Supports live updates via callback functions.

---

## 📦 Development Process

1. **Requirements Analysis**

   * Studied client specifications and defined data and UI needs.

2. **Data Acquisition**

   * Collected rescue dog records from local shelters in Austin, TX.

3. **Database Implementation**

   * Configured MongoDB to store records.
   * Built the `AnimalShelter` module for CRUD operations.

4. **Dashboard Design**

   * Developed layout and interaction model using Dash components.
   * Implemented dropdown filtering, table display, and charts.

5. **Functionality Implementation**

   * Created callback functions for interactive behavior.
   * Integrated geolocation and breed visualizations.

6. **Testing & Deployment**

   * Performed functional testing and bug resolution.
   * Captured demo visuals (screenshots/video) for documentation.

---

## 🚀 Key Features

* ✅ **Mission-Based Filtering** – Easy selection of rescue dog categories.
* 📊 **Live-Updated Data Table** – Instant feedback from the backend.
* 🌎 **Geolocation Chart** – Visual map integration for geographic insight.
* 🐶 **Breed Distribution Pie Chart** – Quickly analyze breed suitability.
* 🎨 **Branded UI** – Includes organization logo and developer ID for traceability.

---
