# 🌍 Incredible India Explorer - AI-Powered Indian Travel Recommender System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 📌 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Dataset](#-dataset)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

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
This creates 3 pickle files:
- `tfidf_vectorizer.pkl`
- `cosine_similarity.pkl`
- `indices.pkl`

### Step 5: Run Application
```bash
streamlit run app_fixed.py
```

Application opens at: `http://localhost:8501`

## 📊 Dataset

### Dataset Statistics
| File | Records | Description |
|------|---------|-------------|
| **Destination_df.csv** | 10,000+ | Destinations across India with details |
| **Users_df.csv** | 10,000+ | User profiles and preferences |
| **Users_History_df.csv** | 10,000+ | Visit history and bookings |
| **Reviews_df.csv** | 10,000+ | User reviews and ratings |

### Key Features in Dataset

**Destination Features:**
- Name, City, State, Type, Tags
- Popularity Score (0-10)
- Rating Count, Best Time to Visit
- Weather Summary, Description
- Latitude, Longitude, Entry Fee
- Average Cost, Recommended Duration
- Activities, Accessibility
- Nearest Airport, Railway Station
- Hotel Information (Name, Price, Booking Link)
- Destination Images

**User History Features:**
- UserID, DestinationID, Preferences
- Trip Purpose, Group Size, Travel Mode
- Cost, Total Spend, Stay Duration
- Booking Source, Weather
- Budget Category, Duration Category
- Experience Rating, Satisfaction Score
- Visit Date

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

## 📸 Screenshots

### Home Page
Beautiful destination cards with images, details, and hotel information.

### Search & Explore
Advanced filters for finding perfect destinations based on preferences.

### Statistics Dashboard
Interactive charts showing trends, distributions, and insights.

### Trending Now
Real-time trending destinations from last 30 days of visitor data.

## 📁 Project Structure

```
incredible-india-explorer/
│
├── app_fixed.py                      # Main Streamlit application
├── train_model.py                    # Model training script (optional)
├── requirements.txt                  # Python dependencies
│
├── Users_df.csv                      # User dataset
├── Destination_df.csv                # Destination dataset
├── Users_History_df.csv              # Visit history dataset
├── Reviews_df.csv                    # Reviews dataset
│
├── tfidf_vectorizer.pkl              # Trained TF-IDF model
├── cosine_similarity.pkl             # Similarity matrix
├── indices.pkl                       # Destination indices
│
├── README.md                         # Project overview (this file)
├── README_HINDI.md                   # Hindi documentation
├── CODE_EXPLANATION.md               # Detailed code explanation
├── CODE_EXPLANATION_HINDI.md         # Hindi code explanation
├── INTERVIEW_QUESTIONS.md            # Interview Q&A
├── QUICK_START.md                    # Quick start guide
└── LICENSE                           # MIT License
```

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

## 👨‍💻 Author

**Your Name**
- GitHub: [@Sumersingpatil2694](https://github.com/Sumersingpatil2694)
- LinkedIn: [Sumersing Patil](https://www.linkedin.com/in/sumersing-patil-839674234/)
- Email: sumerrajput0193@gmail.com

## 🙏 Acknowledgments

- Streamlit for amazing web framework
- Scikit-learn for ML algorithms
- Plotly for interactive visualizations
- Python community for excellent libraries
- Indian tourism data sources

## 📞 Support

For support, email sumerrajput0193@gmail.com or open an issue on GitHub.

---

**⭐ If you like this project, please give it a star!**

**Made with ❤️ for travelers exploring Incredible India**
