# 🌍 Incredible India Explorer - AI-Powered Indian Travel Recommender System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Status]([https://lku3ycfvtzsngc5c2fbexg.streamlit.app/](https://lku3ycfvtzsngc5c2fbexg.streamlit.app/))

## 📌 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Dataset](#-dataset)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [Tech Stack](#-Tech-Stack)


## 🎯 Overview

**Incredible India Explorer** is an intelligent travel recommendation system that helps users discover amazing destinations across India based on their preferences. The system uses **Machine Learning algorithms** (TF-IDF, Cosine Similarity) combined with **popularity-based filtering** to provide personalized destination recommendations.

### 🎪 Purpose & Use Cases

**Why This Project?**
- **Travelers** can discover personalized destinations based on their interests
- **Tourism Businesses** can provide better recommendations to customers
- **Data Analysts** can analyze travel patterns and trends
- **Students & Researchers** can learn about recommendation systems

**Real-World Applications:**
1. **Travel Booking Platforms** - Integrate recommendation engine
2. **Tourism Websites** - Enhance user experience with personalized suggestions
3. **Mobile Travel Apps** - Provide location-based recommendations
4. **Hotel Booking Systems** - Suggest destinations with accommodation
5. **Travel Agencies** - Data-driven travel package creation

## ✨ Features

### 🎯 Core Features
- **AI-Powered Recommendations** - Content-based filtering using TF-IDF and Cosine Similarity
- **Hybrid Recommendation System** - Combines content similarity (70%) + popularity (30%)
- **Advanced Search & Filters** - Search by name, city, state, type, budget, popularity
- **Interactive Dashboard** - Real-time statistics with Plotly visualizations
- **Trending Destinations** - Shows popular destinations from last 30 days
- **User Reviews Integration** - Authentic traveler experiences
- **Hotel Booking Links** - Direct integration with booking platforms

### 🎨 UI/UX Features
- **Modern Dark Theme** - Professional purple gradient design
- **Responsive Layout** - Works on desktop, tablet, and mobile
- **Smooth Animations** - Hover effects and transitions
- **Rich Media Display** - Destination images with fallback support
- **Interactive Charts** - Plotly-powered data visualizations

### 📊 Analytics Features
- **Statistics Dashboard** - Comprehensive data insights
- **State-wise Distribution** - Geographic analysis
- **Budget Analysis** - Cost categorization
- **Type Distribution** - Destination categorization
- **Popularity Trends** - Top destinations ranking

## 🛠️ Tech Stack

### Languages & Frameworks
```
Python 3.8+
Streamlit 1.28+
```

### Core Libraries
```
pandas          - Data manipulation and analysis
numpy           - Numerical computations
scikit-learn    - Machine Learning (TF-IDF, Cosine Similarity)
plotly          - Interactive visualizations
pickle          - Model serialization
```

### Machine Learning Algorithms
1. **TF-IDF Vectorization** - Convert text features to numerical vectors
2. **Cosine Similarity** - Calculate destination similarity scores
3. **Hybrid Filtering** - Combine content + popularity scores

### Frontend & Design
- **Streamlit** - Web framework
- **Custom CSS** - Styled components
- **Plotly Express** - Interactive charts
- **Gradient Design** - Modern UI theme

- > ⚠️ **Deployment Note (Important):**  
> Pre-trained pickle (`.pkl`) models were intentionally **disabled** due to large file size constraints  
> on GitHub and Streamlit Cloud.  
>  
> Instead, the recommendation engine is built **dynamically at runtime** using **TF-IDF vectorization**  
> and **Cosine Similarity**, ensuring:
> - Smooth Streamlit Cloud deployment  
> - No large model files in the repository  
> - Scalable and production-friendly architecture  

## 📥 Installation

### Prerequisites
```bash
Python 3.8 or higher
pip (Python package manager)
```

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/incredible-india-explorer.git
cd incredible-india-explorer
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Add Dataset Files
Place these 4 CSV files in the project root directory:
- `Users_df.csv` (10,000+ users)
- `Destination_df.csv` (10,000+ destinations)
- `Users_History_df.csv` (10,000+ visit records)
- `Reviews_df.csv` (10,000+ reviews)

### Step 4: Train Models (Optional)
```bash
python train_model.py
```
> Note: Model training is optional.  
> The deployed Streamlit app uses an **on-the-fly recommendation engine** and does not require  
> pre-trained `.pkl` files.

This creates 3 pickle files:
- `tfidf_vectorizer.pkl`
- `cosine_similarity.pkl`
- `indices.pkl`

### Step 5: Run Application
```bash
streamlit run app.py
```

Application opens at: `http://localhost:8501`

---

## 📊 Dataset

> **⚠️ Important Note:** This is a **custom-created synthetic dataset** designed specifically for this travel recommendation system project. All data has been generated to represent realistic Indian tourism scenarios.

### 📈 Dataset Overview

This project includes **4 comprehensive CSV datasets** that have been **meticulously created from scratch** to simulate a complete travel ecosystem:

| Dataset File | Records | Size | Description |
|--------------|---------|------|-------------|
| **Destination_df.csv** | 10,000+ | ~7.96 MB | Complete destination information across India |
| **Users_df.csv** | 10,000+ | ~1.71 MB | User profiles and demographics |
| **Users_History_df.csv** | 10,000+ | ~1.40 MB | Travel history and booking records |
| **Reviews_df.csv** | 10,000+ | ~1.45 MB | User reviews and ratings |

**Total Dataset Size:** ~12.52 MB  
**Total Records:** 40,000+

---

### 🗂️ Dataset 1: Destination_df.csv

**Description:** Comprehensive information about tourist destinations across India

**Record Count:** 10,000+ destinations

**Column Structure (33 columns):**

| Column Name | Data Type | Description | Example Values |
|-------------|-----------|-------------|----------------|
| `DestinationID` | Integer | Unique identifier | 1, 2, 3... |
| `Name` | String | Destination name | "Taj Mahal", "Goa Beaches" |
| `City` | String | City location | "Agra", "Panaji" |
| `State/UT` | String | State or Union Territory | "Uttar Pradesh", "Goa" |
| `Type` | String | Destination category | Historical, Beach, Wildlife, Religious, Adventure, Nature |
| `Tags` | String | Comma-separated keywords | "heritage, architecture, iconic" |
| `Popularity` | Float | Rating score (0-10) | 9.48, 8.75 |
| `RatingCount` | Integer | Number of ratings | 284000, 150000 |
| `BestTimeToVisit` | String | Recommended months | "Nov-Feb", "Oct-Mar" |
| `WeatherSummary` | String | Weather description | "Cool 5-25°C, foggy" |
| `Latitude` | Float | Geographic coordinate | 27.1751 |
| `Longitude` | Float | Geographic coordinate | 78.0421 |
| `EntryFee` | Integer | Entrance fee (INR) | 50, 0, 600 |
| `AverageCost` | String | Expected budget range | "1500-3500", "2000-5000" |
| `RecommendedDuration` | String | Suggested visit time | "2-3 hrs", "Full day" |
| `Activities` | String | Available activities | "Photography, sunrise tour" |
| `Accessibility` | String | Accessibility level | "Good", "Partial wheelchair" |
| `NearestAirport` | String | Closest airport | "Agra (AGR)" |
| `NearestRailwayStation` | String | Closest railway station | "Agra Cantt" |
| `Description` | String | Destination overview | "Iconic white marble symbol of love" |
| `DestinationImage` | String | Image URL | "https://upload.wikimedia.org/..." |
| `Hotel1_Name` | String | Hotel option 1 | "Resort Agra" |
| `Hotel1_Link` | String | Booking link | Google search URL |
| `Hotel1_Price` | Integer | Hotel price (INR) | 1908 |
| `Hotel2_Name` | String | Hotel option 2 | "Boutique Hotel Crown" |
| `Hotel2_Link` | String | Booking link | Google search URL |
| `Hotel2_Price` | Integer | Hotel price (INR) | 2284 |
| `Hotel3_Name` | String | Hotel option 3 | "Oberoi Agra" |
| `Hotel3_Link` | String | Booking link | Google search URL |
| `Hotel3_Price` | Integer | Hotel price (INR) | 4140 |
| `Hotel4_Name` | String | Hotel option 4 | "ITC Agra" |
| `Hotel4_Link` | String | Booking link | Google search URL |
| `Hotel4_Price` | Integer | Hotel price (INR) | 6758 |

**Sample Data:**
```
DestinationID: 1
Name: Taj Mahal
City: Agra
State: Uttar Pradesh
Type: Historical
Popularity: 9.48
EntryFee: 50 INR
AverageCost: 1500-3500 INR
```

**Destination Categories:**
- 🏛️ **Historical** (forts, palaces, monuments)
- 🏖️ **Beach** (coastal destinations)
- 🐅 **Wildlife** (national parks, sanctuaries)
- 🕉️ **Religious** (temples, pilgrimage sites)
- ⛰️ **Adventure** (trekking, camping)
- 🌳 **Nature** (hills, valleys, gardens)

---

### 👥 Dataset 2: Users_df.csv

**Description:** User profile information and demographics

**Record Count:** 10,000+ users

**Column Structure (16 columns):**

| Column Name | Data Type | Description | Example Values |
|-------------|-----------|-------------|----------------|
| `UserID` | Integer | Unique identifier | 1, 2, 3... |
| `Name` | String | User full name | "Aanya Iyer", "Rahul Verma" |
| `Age` | Integer | User age | 25, 33, 47 |
| `Gender` | String | Male/Female | "Male", "Female" |
| `City` | String | User's city | "Mumbai", "Delhi" |
| `State` | String | User's state | "Maharashtra", "Delhi" |
| `Country` | String | Always "India" | "India" |
| `Email` | String | Contact email | "aanyaiyer698@rediffmail.com" |
| `PhoneNumber` | Float | Contact number | 918000000000.0 |
| `Address` | String | Residential address | "House 60, Chennai, India" |
| `RegistrationDate` | String | Account creation date | "05-08-2022" |
| `DeviceType` | String | Access device | Web, Android, iOS |
| `Browser` | String | Browser used | Chrome, Firefox, Safari, Edge |
| `OperatingSystem` | String | OS type | Android 14, iOS 17, Windows 11 |
| `IPAddress` | String | IP address | "192.168.29.99" |
| `TrustScore` | Float | Reliability score (0-1) | 0.36, 0.82 |

**Sample Data:**
```
UserID: 1
Name: Aanya Iyer
Age: 33
Gender: Female
City: Chennai
Email: aanyaiyer698@rediffmail.com
```

**Demographics Coverage:**
- **Major Cities:** Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune, Ahmedabad, Jaipur, Lucknow
- **Age Range:** 18-60 years
- **Gender Distribution:** Balanced male/female representation
- **Device Types:** Web, Android, iOS

---

### 📅 Dataset 3: Users_History_df.csv

**Description:** Travel history and booking records

**Record Count:** 10,000+ travel records

**Column Structure (16 columns):**

| Column Name | Data Type | Description | Example Values |
|-------------|-----------|-------------|----------------|
| `UserID` | Integer | User reference | 1, 2, 3... |
| `DestinationID` | Integer | Destination reference | 1883, 3592 |
| `Preferences` | String | User preference type | Leisure, Business, Religious, Family, Adventure |
| `TripPurpose` | String | Travel reason | Honeymoon, Business, Family, Leisure, Religious, Adventure |
| `GroupSize` | String | Travel group | Solo, Couple, Family, Group |
| `TravelMode` | String | Transportation | Flight, Train, Car, Cab, Bike |
| `Cost` | Integer | Base travel cost (INR) | 43036, 6170 |
| `TotalSpend` | Integer | Total expenditure (INR) | 44236, 15770 |
| `StayDuration` | Integer | Days stayed | 1, 7, 8 |
| `BookingSource` | String | Booking platform | MakeMyTrip, Yatra, Booking.com, Goibibo, Cleartrip |
| `Weather` | String | Weather condition | Sunny, Rainy, Cold, Pleasant |
| `BudgetCategory` | String | Budget classification | Low Budget, Medium Budget, Luxury |
| `DurationCategory` | String | Trip length | Short Trip (1-2 days), Medium Trip (3-5 days), Long Trip (6+ days) |
| `ExperienceRating` | Integer | Trip rating (1-10) | 8, 9, 10 |
| `SatisfactionScore` | String | Satisfaction level | Highly Satisfied, Satisfied, Neutral, Unsatisfied |
| `VisitDate` | String | Travel date | "03-08-2021" |

**Sample Data:**
```
UserID: 1
DestinationID: 1883
TripPurpose: Business
GroupSize: Couple
TravelMode: Cab
TotalSpend: 44236 INR
StayDuration: 1 day
```

**Travel Patterns Captured:**
- **Budget Categories:**
  - Low Budget: ₹0 - ₹20,000
  - Medium Budget: ₹20,001 - ₹50,000
  - Luxury: ₹50,001+
  
- **Trip Durations:**
  - Short Trip: 1-2 days
  - Medium Trip: 3-5 days
  - Long Trip: 6+ days

- **Booking Platforms:** MakeMyTrip, Yatra, Booking.com, Goibibo, Cleartrip

---

### ⭐ Dataset 4: Reviews_df.csv

**Description:** User-generated reviews and ratings

**Record Count:** 10,000+ reviews

**Column Structure (7 columns):**

| Column Name | Data Type | Description | Example Values |
|-------------|-----------|-------------|----------------|
| `ReviewID` | Integer | Unique identifier | 1, 2, 3... |
| `DestinationID` | Integer | Destination reference | 1824, 4325 |
| `UserID` | Integer | User reference | 1893, 623 |
| `Rating` | Integer | Star rating (1-5) | 1, 2, 3, 4, 5 |
| `Title` | String | Review headline | "Amazing Experience!", "Worth the Trip" |
| `ReviewText` | String | Detailed review | "I visited Shimla recently..." |
| `Date` | String | Review date | "24-11-2022" |

**Sample Data:**
```
ReviewID: 1
DestinationID: 1824
UserID: 1893
Rating: 2
Title: "Worth the Trip"
ReviewText: "I visited Serolsar Lake Trek recently..."
Date: "24-11-2022"
```

**Review Titles (Variety):**
- "Amazing Experience!"
- "Worth the Trip"
- "Highly Recommended"
- "Loved It!"
- "Not as Expected"
- "Crowded but Fun"
- "Memorable Visit"
- "A Peaceful Getaway"
- "Could Be Better"
- "Fantastic Place"

---

### 🔗 Dataset Relationships

```
┌─────────────────┐
│   Users_df      │
│   (UserID)      │
└────────┬────────┘
         │
         ├──────────┐
         │          │
         ▼          ▼
┌─────────────┐  ┌──────────────────┐
│ Reviews_df  │  │ Users_History_df │
│ (ReviewID)  │  │ (VisitDate)      │
└──────┬──────┘  └────────┬─────────┘
       │                  │
       │                  │
       └─────────┬────────┘
                 │
                 ▼
       ┌──────────────────┐
       │  Destination_df  │
       │  (DestinationID) │
       └──────────────────┘
```

**Relationships:**
1. `Users_df.UserID` → `Users_History_df.UserID` (One-to-Many)
2. `Users_df.UserID` → `Reviews_df.UserID` (One-to-Many)
3. `Destination_df.DestinationID` → `Users_History_df.DestinationID` (One-to-Many)
4. `Destination_df.DestinationID` → `Reviews_df.DestinationID` (One-to-Many)

---

### 📍 Geographic Coverage

**States/UTs Covered (36):**
- Uttar Pradesh
- Rajasthan
- Goa
- Kerala
- Ladakh
- Maharashtra
- Karnataka
- Madhya Pradesh
- West Bengal
- Assam
- Uttarakhand
- Jammu and Kashmir
- Andaman and Nicobar Islands
- Punjab
- Odisha
- Bihar
- Delhi
- Tamil Nadu
- Himachal Pradesh
- Sikkim
- Gujarat
- Telangana
- And more...

---

### 🎲 Data Generation Methodology

**How This Dataset Was Created:**

1. **Research Phase:**
   - Studied real Indian tourism data
   - Analyzed popular travel platforms
   - Researched destination characteristics

2. **Data Structure Design:**
   - Designed comprehensive schema
   - Defined relationships between tables
   - Ensured data consistency

3. **Synthetic Data Generation:**
   - Created realistic destination profiles
   - Generated diverse user demographics
   - Simulated authentic travel patterns
   - Crafted varied review content

4. **Quality Assurance:**
   - Validated data accuracy
   - Checked for consistency
   - Ensured realistic distributions
   - Tested relationships

---

### 🎯 Dataset Use Cases

**For Students & Learners:**
- Practice data analysis with pandas
- Learn recommendation algorithms
- Understand travel industry data
- Build portfolio projects

**For Researchers:**
- Study tourism patterns
- Analyze user behavior
- Test ML algorithms
- Conduct statistical analysis

**For Developers:**
- Build travel applications
- Test recommendation systems
- Create data visualizations
- Develop booking platforms

---

### 📝 Dataset Citation

If you use this dataset in your research or project, please cite:

```
@dataset{incredible_india_explorer_2024,
  title={Incredible India Explorer Travel Dataset},
  author={[Your Name]},
  year={2024},
  description={Synthetic dataset for Indian travel recommendation system},
  records={40000+},
  size={12.52 MB}
}
```

---

### ⚖️ Data License & Usage

**License:** This dataset is created for **educational and research purposes**.

**Allowed Uses:**
✅ Academic research  
✅ Educational projects  
✅ Portfolio demonstrations  
✅ Algorithm testing  
✅ Non-commercial applications  

**Restrictions:**
❌ Commercial use without permission  
❌ Claiming as real data  
❌ Redistribution without attribution  

---

### 🔍 Data Quality Metrics

| Metric | Value | Description |
|--------|-------|-------------|
| **Completeness** | 99.8% | Minimal missing values |
| **Consistency** | 100% | All relationships valid |
| **Accuracy** | Realistic | Based on real patterns |
| **Diversity** | High | Wide range of scenarios |
| **Volume** | 40,000+ | Large enough for ML |

---

## 🚀 Usage

### Basic Usage

1. **Home Page** - Browse popular destinations
2. **Search Box** - Type destination name, city, or tags
3. **Filters** - Apply type, state, budget, popularity filters
4. **Get Recommendations** - Click on any destination card
5. **View Statistics** - Explore data insights and trends

### Advanced Features

**Smart Search:**
```
Search across: Name, City, State, Tags, Type, Description, Activities
Example: "Goa", "Beach", "Wildlife", "Temple", "Kerala"
```

**Filters:**
- **Type Filter** - Historical, Religious, Beach, Wildlife, Adventure
- **State Filter** - Select from 36 states and UTs
- **Budget Filter** - ₹0 to ₹200,000
- **Popularity Filter** - 0 to 10 rating

**Sorting Options:**
- Popularity (High to Low / Low to High)
- Cost (Low to High / High to Low)
- Name (A-Z)

### Recommendation System

**How it Works:**

1. **Content-Based Filtering**
   - Uses TF-IDF on destination tags, description, activities
   - Calculates cosine similarity between destinations
   - Finds similar destinations based on features

2. **Hybrid Approach**
   - Combines content similarity (70%) + popularity (30%)
   - Balances personalized recommendations with popular choices
   - Provides diverse and relevant suggestions

**Getting Recommendations:**
1. Click on any destination card
2. Click "🎯 Get Similar Destinations" button
3. View top 4-6 similar destinations

---

## 📸 Screenshots

### Home Page
Beautiful destination cards with images, details, and hotel information.

### Search & Explore
Advanced filters for finding perfect destinations based on preferences.

### Statistics Dashboard
Interactive charts showing trends, distributions, and insights.

### Trending Now
Real-time trending destinations from last 30 days of visitor data.

---

## 📁 Project Structure

```
incredible-india-explorer/
│
├── app.py                            # Main Streamlit application
├── train_model.py                    # Model training script (optional)
├── requirements.txt                  # Python dependencies
│
├── Users_df.csv                      # User dataset (Custom Created)
├── Destination_df.csv                # Destination dataset (Custom Created)
├── Users_History_df.csv              # Visit history dataset (Custom Created)
├── Reviews_df.csv                    # Reviews dataset (Custom Created)
│
├── tfidf_vectorizer.pkl              # Trained TF-IDF model
├── cosine_similarity.pkl             # Similarity matrix
├── indices.pkl                       # Destination indices
│
├── README.md                         # Project documentation
└── QUICK_START.md                     # Quick start guide
                          
```

---

## 🎓 Learning Outcomes

### Technical Skills
- **Machine Learning** - Content-based recommendation systems
- **Natural Language Processing** - TF-IDF vectorization
- **Data Science** - Pandas, NumPy for data analysis
- **Web Development** - Streamlit framework
- **Data Visualization** - Plotly charts and graphs
- **Python Programming** - Advanced Python concepts

### Domain Knowledge
- **Tourism Industry** - Understanding travel patterns
- **User Behavior Analysis** - Preference patterns
- **Recommendation Systems** - Hybrid filtering approaches
- **Data Engineering** - Large dataset handling
- **Dataset Creation** - Synthetic data generation

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Areas for Contribution
- Add more ML algorithms (Collaborative Filtering, Neural Networks)
- Improve UI/UX design
- Add user authentication
- Implement booking system
- Create mobile app version
- Add multi-language support
- Integrate real-time data APIs
- Expand dataset with more destinations

---

## 👨‍💻 Author

**Sumersing Patil**
- GitHub: [@Sumersingpatil2694](https://github.com/Sumersingpatil2694)
- LinkedIn: [Sumersing Patil](https://www.linkedin.com/in/sumersing-patil-839674234/)
- Email:sumerrajput0193@gmail.com

---

## 🙏 Acknowledgments

- Streamlit for amazing web framework
- Scikit-learn for ML algorithms
- Plotly for interactive visualizations
- Python community for excellent libraries
- Indian tourism for inspiration

---

## 📞 Support

For support, sumerrajput0193@gmail.com.com or open an issue on GitHub.

---

## ⭐ Star History

If you find this project helpful, please give it a ⭐ on GitHub!

---

**⭐ If you like this project, please give it a star!**

**Made with ❤️ for travelers exploring Incredible India**

---

## 🔖 Keywords

`travel-recommendation` `machine-learning` `india-tourism` `streamlit` `python` `data-science` `recommendation-system` `content-based-filtering` `tfidf` `cosine-similarity` `tourism-data` `travel-app` `indian-destinations` `synthetic-dataset` `custom-dataset`
