import streamlit as st
import pandas as pd
import pickle
from datetime import datetime, timedelta
import warnings
import plotly.express as px
import plotly.graph_objects as go

warnings.filterwarnings("ignore")

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Incredible India Explorer – AI-Powered Travel Recommendation System",
    page_icon="✈️🇮🇳",
    layout="wide"
)


# =========================================================
# ENHANCED CSS WITH PROPER COLORS
# =========================================================
st.markdown("""
<style>
    /* Main theme */
    .main {
        background-color: #0e1117;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
    }
    
    .main-header h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .main-header p {
    font-size: 1.2rem;
    font-weight: 500;
    color: #f9fafb;   /* pure white */

    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    }
    
    /* Card styling */
    .destination-card {
        background: linear-gradient(145deg, #1e1e2e 0%, #252538 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
        margin-bottom: 2rem;
        border: 1px solid #333;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        color: #ffffff;
    }
    
    .destination-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Stats card */
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    .stats-number {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
    font-size: 1rem;
    font-weight: 500;
    color: #f1f5f9;   /* clean light color */

    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    }
    
    /* Destination info */
    .dest-title {
    color: #f9fafb;            /* pure white – sharp */
    font-size: 1.9rem;
    font-weight: 800;
    letter-spacing: 0.3px;

    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    
    }
    
    .dest-info {
    color: #e5e7eb;
    font-size: 1rem;
    font-weight: 500;
    line-height: 1.8;

    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
            
    }
    
    .dest-description {
    color: #d1d5db;
    font-size: 0.95rem;
    font-weight: 400;
    line-height: 1.7;

    text-rendering: optimizeLegibility;

    }
    
    /* Tags */
    .tag {
        display: inline-block;
        background: rgba(102, 126, 234, 0.2);
        color: #667eea;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 0.2rem;
        border: 1px solid rgba(102, 126, 234, 0.3);
    }
    
    /* Hotel section */
    .hotel-section {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .hotel-name {
        color: #ffd700;
        font-size: 1.1rem;
        font-weight: 600;
    }
    
    .hotel-price {
        color: #4ade80;
        font-size: 1rem;
        font-weight: 600;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.5);
        transform: translateY(-2px);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1e1e2e;
    }
    
    /* Review card */
    .review-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        color: #e0e0e0;
    }
    
    /* Image container */
    .img-container {
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    
    /* Search box styling */
    .stTextInput > div > div > input {
        background-color: #1e1e2e;
        color: white;
        border: 2px solid #667eea;
        border-radius: 10px;
        padding: 0.75rem;
        font-size: 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    try:
        users = pd.read_csv("Users_df.csv")
        destinations = pd.read_csv("Destination_df.csv")
        # Clean DestinationImage column
        if "DestinationImage" in destinations.columns:
            destinations["DestinationImage"] = (
                destinations["DestinationImage"]
                .astype(str)
                .str.strip()
                .replace("nan", "")
            )

        history = pd.read_csv("Users_History_df.csv")
        reviews = pd.read_csv("Reviews_df.csv")
        
        # Clean and fill missing values
        for col in ["Description", "Activities", "Type", "BestTimeToVisit", "WeatherSummary"]:
            if col in destinations.columns:
                destinations[col] = destinations[col].fillna("Not specified")
        
        # Handle destination images (USE DATASET IMAGE ONLY)
        if "DestinationImage" in destinations.columns:
           destinations["DestinationImage"] = (
           destinations["DestinationImage"]
           .astype(str)
           .str.strip()
           .replace("nan", "")
        )

        
        # Handle tags
        if "Tags" in destinations.columns:
            destinations["Tags"] = destinations["Tags"].fillna("")
        
        # Convert dates
        if "VisitDate" in history.columns:
            history["VisitDate"] = pd.to_datetime(history["VisitDate"], errors="coerce", dayfirst=True)
        
        return users, destinations, history, reviews
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None, None, None

# =========================================================
# LOAD MODELS
# =========================================================
@st.cache_resource
def load_models():
    try:
        tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))
        cosine_sim = pickle.load(open("cosine_similarity.pkl", "rb"))
        indices = pickle.load(open("indices.pkl", "rb"))
        return tfidf, cosine_sim, indices
    except:
        st.warning("⚠️ Recommendation models not found. Some features may be limited.")
        return None, None, None

# =========================================================
# UTILITY FUNCTIONS
# =========================================================
def parse_average_cost(cost_value):
    """Convert average cost to numeric value"""
    if pd.isna(cost_value):
        return 0
    if isinstance(cost_value, (int, float)):
        return int(cost_value)
    cost_str = str(cost_value).replace("₹", "").replace(",", "").strip()
    # Handle range like "50000-121268"
    if "-" in cost_str:
        cost_str = cost_str.split("-")[0].strip()
    try:
        return int(float(cost_str))
    except:
        return 0

# =========================================================
# RECOMMENDATION FUNCTIONS
# =========================================================
def get_content_recommendations(name, cosine_sim, indices, df, top_n=6):
    """Get content-based recommendations"""
    if name not in indices:
        return pd.DataFrame()
    
    idx = indices[name]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
    rec_idx = [i[0] for i in scores]
    recs = df.iloc[rec_idx].copy()
    recs["Similarity_Score"] = [round(i[1], 3) for i in scores]
    return recs

def get_hybrid_recommendations(name, cosine_sim, indices, df, top_n=6):
    """Get hybrid recommendations (content + popularity)"""
    recs = get_content_recommendations(name, cosine_sim, indices, df, top_n)
    
    if recs.empty:
        return recs
    
    if "Popularity" in recs.columns:
        # Normalize popularity for scoring
        max_pop = df["Popularity"].max()
        recs["NormPopularity"] = recs["Popularity"] / max_pop if max_pop > 0 else 0
        recs["FinalScore"] = (recs["Similarity_Score"] * 0.7 + recs["NormPopularity"] * 0.3)
        recs = recs.sort_values("FinalScore", ascending=False)
    
    return recs

# =========================================================
# DESTINATION CARD WITH IMAGES
# =========================================================
def destination_card(row, show_recommend_btn=False, cosine_sim=None, indices=None, destinations=None):
    """Enhanced destination card with proper image display"""
    
    st.markdown('<div class="destination-card">', unsafe_allow_html=True)
    
    # Image display
    img_url = row.get("DestinationImage")
    
    st.markdown('<div class="img-container">', unsafe_allow_html=True)

    if isinstance(img_url, str) and img_url.strip() != "":
        st.image(img_url.strip(), use_container_width=True)
    else:
        st.image(
            "https://via.placeholder.com/800x400?text=No+Image",
            use_container_width=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # Title and basic info
    st.markdown(f'<div class="dest-title">🌟 {row.get("Name", "Unknown")}</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="dest-info">
        📍 <b>Location:</b> {row.get("City", "")}, {row.get("State/UT", "")}<br>
        🏷️ <b>Type:</b> {row.get("Type", "")}<br>
        ⭐ <b>Popularity:</b> {row.get("Popularity", "N/A")}/10<br>
        💬 <b>Reviews:</b> {row.get("RatingCount", "N/A"):,}<br>
        🌤️ <b>Best Time:</b> {row.get("BestTimeToVisit", "")}<br>
        ☁️ <b>Weather:</b> {row.get("WeatherSummary", "")}<br>
        🚆 <b>Nearest Railway Station:</b> {row.get("NearestRailwayStation", "Not available")}<br>
        ✈️ <b>Nearest Airport:</b> {row.get("NearestAirport", "Not available")}
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Stats
        if pd.notna(row.get("AverageCost")):
            avg_cost = parse_average_cost(row.get("AverageCost"))
            st.markdown(f'<div class="stats-card"><div class="stats-number">₹{avg_cost:,}</div>'
                       f'<div class="stats-label">Avg Cost</div></div>',
                       unsafe_allow_html=True)
    
    # Description
    desc = str(row.get("Description", ""))
    if desc and desc != "Not specified":
        st.markdown(f'<div class="dest-description">📝 {desc[:300]}...</div>', unsafe_allow_html=True)
    
    # Tags
    tags = str(row.get("Tags", ""))
    if tags and tags != "":
        tag_list = [t.strip() for t in tags.split(",")[:6]]
        tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in tag_list])
        st.markdown(f'<div style="margin: 1rem 0;">{tags_html}</div>', unsafe_allow_html=True)
    
    # Activities
    activities = str(row.get("Activities", ""))
    if activities and activities != "Not specified":
        st.markdown(f'**🎯 Activities:** {activities[:150]}...')
    
    # Hotel Section
    st.markdown('<div class="hotel-section">', unsafe_allow_html=True)
    st.markdown("### 🏨 Recommended Hotels")
    
    hotel_cols = st.columns(2)
    
    for i, col in enumerate(hotel_cols[:2]):
        hotel_num = i + 1
        hotel_name = row.get(f"Hotel{hotel_num}_Name", "")
        hotel_link = row.get(f"Hotel{hotel_num}_Link", "#")
        hotel_price = row.get(f"Hotel{hotel_num}_Price", "")
        
        if pd.notna(hotel_name) and hotel_name:
            with col:
                st.markdown(f'<div class="hotel-name">🏨 {hotel_name}</div>', unsafe_allow_html=True)
                if pd.notna(hotel_price):
                    st.markdown(f'<div class="hotel-price">💰 ₹{hotel_price:,}/night</div>', unsafe_allow_html=True)
                if pd.notna(hotel_link) and hotel_link != "#":
                    st.markdown(f'[🔗 Book Now]({hotel_link})')
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Recommend button
    if show_recommend_btn and cosine_sim is not None:
        if st.button(f"🎯 Get Similar Destinations", key=f"rec_{row.get('DestinationID', row.get('Name'))}"):
            st.session_state[f"show_recs_{row.get('Name')}"] = True
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show recommendations if button clicked
    if show_recommend_btn and cosine_sim is not None:
        if st.session_state.get(f"show_recs_{row.get('Name')}", False):
            st.markdown("---")
            st.subheader(f"🎯 Similar to {row.get('Name')}")
            recs = get_hybrid_recommendations(row.get("Name"), cosine_sim, indices, destinations, top_n=4)
            
            if not recs.empty:
                for _, rec_row in recs.iterrows():
                    destination_card(rec_row)
            else:
                st.info("No similar destinations found.")

# =========================================================
# STATISTICS DASHBOARD
# =========================================================
def show_statistics(users, destinations, history, reviews):
    """Display statistics dashboard"""
    
    st.markdown('<div class="main-header"><h1>📊 Statistics Dashboard</h1></div>', unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{len(destinations):,}</div>
            <div class="stats-label">Destinations</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{len(users):,}</div>
            <div class="stats-label">Users</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{len(reviews):,}</div>
            <div class="stats-label">Reviews</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        total_visits = len(history) if history is not None else 0
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-number">{total_visits:,}</div>
            <div class="stats-label">Total Visits</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Top destinations by popularity
        st.subheader("🔥 Top 10 Popular Destinations")
        top_dest = destinations.nlargest(10, "Popularity")[["Name", "Popularity"]]
        fig = px.bar(top_dest, x="Popularity", y="Name", orientation="h",
                     color="Popularity", color_continuous_scale="Viridis")
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Destinations by type
        st.subheader("🏷️ Destinations by Type")
        type_count = destinations["Type"].value_counts().head(10)
        fig = px.pie(values=type_count.values, names=type_count.index, hole=0.4)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # State-wise distribution
    st.subheader("📍 State-wise Distribution")
    state_count = destinations["State/UT"].value_counts().head(15)
    fig = px.bar(x=state_count.index, y=state_count.values,
                 labels={"x": "State", "y": "Number of Destinations"},
                 color=state_count.values, color_continuous_scale="Blues")
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Budget distribution
    st.subheader("💰 Budget Distribution")
    if "BudgetCategory" in history.columns:
        budget_dist = history["BudgetCategory"].value_counts()
        fig = px.bar(x=budget_dist.index, y=budget_dist.values,
                     labels={"x": "Budget Category", "y": "Count"},
                     color=budget_dist.values, color_continuous_scale="Greens")
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# MAIN APP
# =========================================================
def main():
    # Load data
    users, destinations, history, reviews = load_data()
    
    if destinations is None:
        st.error("❌ Failed to load data. Please check if CSV files are present.")
        return
    
    tfidf, cosine_sim, indices = load_models()
    
    # HEADER
    st.markdown("""
    <div class="main-header">
        <h1>🌍🚀 Incredible India Explorer</h1>
        <p>AI-Powered Travel Recommendation System</p>
    </div>
    """, unsafe_allow_html=True)
    
    # SIDEBAR NAVIGATION
    st.sidebar.markdown("## 🏠 Home")
    page = st.sidebar.radio(
        "Go to:",
        ["🏠 Home", "🔍 Search & Explore", "🔥 Trending Now", "📊 Statistics", 
         "⭐ Find by Type", "💬 Reviews", "ℹ️ About"],
        label_visibility="collapsed"
    )
    
    # =====================================================
    # HOME PAGE - ENHANCED SEARCH FUNCTIONALITY
    # =====================================================
    if page == "🏠 Home":
        st.subheader("🌟 Most Popular Destinations")
        
        # ========================================
        # 🔍 ENHANCED SEARCH WITH BETTER FILTERING
        # ========================================
        search_query = st.text_input(
            "🔍 Search destinations by name, city, state or tags",
            placeholder="e.g., Goa, Pune, Wildlife, Kerala, Beach, Temple...",
            key="home_search"
        )
        
        # START WITH ALL DESTINATIONS FOR SEARCH, NOT JUST TOP 12
        if search_query and search_query.strip():
            search_term = search_query.strip().lower()  # Convert to lowercase for better matching
            
            # Search across ALL destinations, not just top 12
            mask = (
                destinations["Name"].str.lower().str.contains(search_term, na=False) |
                destinations["City"].str.lower().str.contains(search_term, na=False) |
                destinations["State/UT"].str.lower().str.contains(search_term, na=False) |
                destinations["Tags"].str.lower().str.contains(search_term, na=False) |
                destinations["Type"].str.lower().str.contains(search_term, na=False) |
                destinations["Description"].str.lower().str.contains(search_term, na=False) |
                destinations["Activities"].str.lower().str.contains(search_term, na=False)
            )
            
            display_destinations = destinations[mask].copy()
            
            # If search results found, sort by popularity
            if not display_destinations.empty:
                display_destinations = display_destinations.sort_values("Popularity", ascending=False).head(20)
                st.success(f"✅ Found {len(destinations[mask])} destination(s) matching '{search_query}' - Showing top {len(display_destinations)}")
            else:
                # No results found - show popular destinations
                st.warning(f"❌ No destinations found for '{search_query}'. Showing popular destinations instead.")
                display_destinations = destinations.nlargest(12, "Popularity")
        else:
            # No search query - show top 12 popular destinations
            display_destinations = destinations.nlargest(12, "Popularity")
        
        # Display destinations
        for _, row in display_destinations.iterrows():
            destination_card(
                row,
                show_recommend_btn=True,
                cosine_sim=cosine_sim,
                indices=indices,
                destinations=destinations
            )
    
    # =====================================================
    # SEARCH & EXPLORE
    # =====================================================
    elif page == "🔍 Search & Explore":
        st.subheader("🔍 Search Destinations")
        
        # Search filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_query = st.text_input("🔎 Search by name, city or state", "")
        
        with col2:
            dest_types = ["All"] + sorted(destinations["Type"].dropna().unique().tolist())
            selected_type = st.selectbox("🏷️ Filter by Type", dest_types)
        
        with col3:
            states = ["All"] + sorted(destinations["State/UT"].dropna().unique().tolist())
            selected_state = st.selectbox("📍 Filter by State", states)
        
        # Additional filters
        col4, col5 = st.columns(2)
        
        with col4:
            min_popularity = st.slider("⭐ Minimum Popularity", 0.0, 10.0, 0.0, 0.1)
        
        with col5:
            max_cost = st.slider("💰 Maximum Cost (₹)", 0, 200000, 200000, 5000)
        
        # Apply filters
        filtered = destinations.copy()
        
        if search_query:
            search_term = search_query.strip().lower()
            mask = (
                filtered["Name"].str.lower().str.contains(search_term, na=False) |
                filtered["City"].str.lower().str.contains(search_term, na=False) |
                filtered["State/UT"].str.lower().str.contains(search_term, na=False) |
                filtered["Tags"].str.lower().str.contains(search_term, na=False) |
                filtered["Type"].str.lower().str.contains(search_term, na=False) |
                filtered["Description"].str.lower().str.contains(search_term, na=False) |
                filtered["Activities"].str.lower().str.contains(search_term, na=False)
            )
            filtered = filtered[mask]
        
        if selected_type != "All":
            filtered = filtered[filtered["Type"] == selected_type]
        
        if selected_state != "All":
            filtered = filtered[filtered["State/UT"] == selected_state]
        
        filtered = filtered[filtered["Popularity"] >= min_popularity]
        filtered["AvgCost_Num"] = filtered["AverageCost"].apply(parse_average_cost)
        filtered = filtered[filtered["AvgCost_Num"] <= max_cost]
        
        # Sort options
        sort_by = st.selectbox("Sort by:", ["Popularity (High to Low)", "Popularity (Low to High)", 
                                             "Cost (Low to High)", "Cost (High to Low)", "Name (A-Z)"])
        
        if sort_by == "Popularity (High to Low)":
            filtered = filtered.sort_values("Popularity", ascending=False)
        elif sort_by == "Popularity (Low to High)":
            filtered = filtered.sort_values("Popularity", ascending=True)
        elif sort_by == "Cost (Low to High)":
            filtered = filtered.sort_values("AvgCost_Num", ascending=True)
        elif sort_by == "Cost (High to Low)":
            filtered = filtered.sort_values("AvgCost_Num", ascending=False)
        else:
            filtered = filtered.sort_values("Name")
        
        # Display results
        st.markdown(f"### Found {len(filtered)} destinations")
        
        if len(filtered) == 0:
            st.warning("No destinations found matching your criteria.")
        else:
            for _, row in filtered.head(20).iterrows():
                destination_card(row, show_recommend_btn=True, cosine_sim=cosine_sim,
                               indices=indices, destinations=destinations)
    
    # =====================================================
    # TRENDING NOW
    # =====================================================
    elif page == "🔥 Trending Now":
        st.subheader("🔥 Trending Destinations")
        
        if history is not None and len(history) > 0:
            # Get trending from last 30 days
            recent_date = datetime.now() - timedelta(days=30)
            recent = history[history["VisitDate"] >= recent_date]
            
            if len(recent) > 0:
                trending = (
                    recent.groupby("DestinationID")
                    .size()
                    .sort_values(ascending=False)
                    .head(10)
                    .reset_index(name="Visits")
                )
                
                trending = trending.merge(destinations, on="DestinationID", how="left")
                
                st.info(f"📊 Showing top 10 destinations from last 30 days ({len(recent)} total visits)")
                
                for _, row in trending.iterrows():
                    st.markdown(f"**🔥 {int(row['Visits'])} visits in last 30 days**")
                    destination_card(row, show_recommend_btn=True, cosine_sim=cosine_sim,
                                   indices=indices, destinations=destinations)
            else:
                st.info("No visits in last 30 days. Showing most popular destinations.")
                top_dest = destinations.nlargest(10, "Popularity")
                for _, row in top_dest.iterrows():
                    destination_card(row, show_recommend_btn=True, cosine_sim=cosine_sim,
                                   indices=indices, destinations=destinations)
        else:
            st.info("No visit history data available. Showing most popular destinations.")
            top_dest = destinations.nlargest(10, "Popularity")
            for _, row in top_dest.iterrows():
                destination_card(row, show_recommend_btn=True, cosine_sim=cosine_sim,
                               indices=indices, destinations=destinations)
    
    # =====================================================
    # STATISTICS
    # =====================================================
    elif page == "📊 Statistics":
        show_statistics(users, destinations, history, reviews)
    
    # =====================================================
    # FIND BY TYPE
    # =====================================================
    elif page == "⭐ Find by Type":
        st.subheader("🏷️ Find Destinations by Type")
        
        types = sorted(destinations["Type"].dropna().unique().tolist())
        
        selected = st.selectbox("Select destination type:", types)
        
        filtered = destinations[destinations["Type"] == selected].nlargest(10, "Popularity")
        
        st.info(f"Found {len(filtered)} top destinations")
        
        for _, row in filtered.iterrows():
            destination_card(row, show_recommend_btn=True, cosine_sim=cosine_sim,
                           indices=indices, destinations=destinations)
    
    # =====================================================
    # REVIEWS
    # =====================================================
    elif page == "💬 Reviews":
        st.subheader("💬 Recent Reviews")
        
        if reviews is not None and len(reviews) > 0:
            # Get recent reviews
            recent_reviews = reviews.nlargest(20, "ReviewID")
            
            for _, review in recent_reviews.iterrows():
                # Get destination name
                dest_id = review.get("DestinationID")
                dest_name = destinations[destinations["DestinationID"] == dest_id]["Name"].values
                dest_name = dest_name[0] if len(dest_name) > 0 else "Unknown"
                
                rating = "⭐" * int(review.get("Rating", 0))
                
                st.markdown(f"""
                <div class="review-card">
                    <h4>{dest_name}</h4>
                    <div>{rating} {review.get('Rating', 0)}/5</div>
                    <h5>{review.get('Title', '')}</h5>
                    <p>{review.get('ReviewText', '')[:200]}...</p>
                    <small>📅 {review.get('Date', '')}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No reviews available.")
    
    # =====================================================
    # ABOUT
    # =====================================================
    elif page == "ℹ️ About":
        st.subheader("ℹ️ About Incredible India Explorer")
        
        st.markdown("""
        <div class="destination-card">
        <h2>🌍 Incredible India Explorer – AI-Powered Travel Recommendation System</h2>
        
        <p>Incredible India Explorer is an intelligent travel recommendation system designed to help you discover 
        amazing destinations across India based on your preferences.</p>
        
        <h3>✨ Key Features:</h3>
        <ul>
            <li>🎯 <b>AI-Powered Recommendations</b> - Get personalized destination suggestions</li>
            <li>🔍 <b>Advanced Search & Filters</b> - Find destinations by type, budget, location</li>
            <li>📊 <b>Statistics Dashboard</b> - Visualize trends and insights</li>
            <li>🏨 <b>Hotel Integration</b> - Direct booking links for accommodations</li>
            <li>💬 <b>User Reviews</b> - Read authentic experiences from travelers</li>
            <li>🔥 <b>Trending Destinations</b> - See what's popular right now</li>
            <li>📸 <b>Rich Media</b> - Beautiful destination images and details</li>
        </ul>
        
        <h3>🔧 Technology Stack:</h3>
        <ul>
            <li>Python & Streamlit</li>
            <li>Pandas for data processing</li>
            <li>Scikit-learn (TF-IDF, Cosine Similarity)</li>
            <li>Plotly for interactive visualizations</li>
        </ul>
        
        <h3>📊 Dataset:</h3>
        <ul>
            <li><b>10,000+</b> Destinations across India</li>
            <li><b>10,000+</b> User profiles</li>
            <li><b>10,000+</b> Reviews</li>
            <li><b>10,000+</b> Visit history records</li>
        </ul>
        
        <h3>🚀 How to Use:</h3>
        <ol>
            <li><b>Browse</b> popular destinations on the home page</li>
            <li><b>Search</b> for specific places using the search box</li>
            <li><b>Get Recommendations</b> by clicking on destination cards</li>
            <li><b>Explore</b> trending destinations and statistics</li>
            <li><b>Read Reviews</b> from other travelers</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
