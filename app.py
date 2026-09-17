import streamlit as st
import pandas as pd


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="CSV Data Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* ==================================================
   GLOBAL
   ================================================== */

.main {
    background-color: #f7f8fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* ==================================================
   SIDEBAR
   ================================================== */

[data-testid="stSidebar"] {
    background-color: #111827 !important;
}


/* ==================================================
   SIDEBAR DEFAULT TEXT
   ================================================== */

/* Do NOT use:
   [data-testid="stSidebar"] * {
       color: #f9fafb;
   }
   
   because it makes the uploaded file text white.
*/


[data-testid="stSidebar"] .stMarkdown {
    color: #f9fafb;
}


/* Sidebar headings */

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h4 {
    color: #ffffff !important;
}


/* ==================================================
   SIDEBAR TITLE
   ================================================== */

.sidebar-title {
    color: #ffffff !important;

    font-size: 22px;

    font-weight: 700;

    margin-bottom: 6px;
}


/* ==================================================
   SIDEBAR SUBTITLE
   ================================================== */

.sidebar-subtitle {
    color: #9ca3af !important;

    font-size: 13px;

    font-weight: 400;

    margin-bottom: 25px;
}


/* ==================================================
   UPLOAD TITLE
   ================================================== */

.upload-title {
    color: #ffffff !important;

    font-size: 18px;

    font-weight: 700;

    margin-top: 8px;

    margin-bottom: 14px;
}


/* ==================================================
   FILE UPLOADER
   ================================================== */

[data-testid="stFileUploader"] {
    background: transparent !important;

    border: none !important;

    padding: 0 !important;

    margin: 0 !important;
}


/* ==================================================
   UPLOAD DROPZONE
   ================================================== */

[data-testid="stFileUploaderDropzone"] {

    background-color: #f8fafc !important;

    border: 1.5px dashed #cbd5e1 !important;

    border-radius: 16px !important;

    padding: 24px !important;

    transition:
        background-color 0.2s ease,
        border-color 0.2s ease,
        box-shadow 0.2s ease !important;
}


/* ==================================================
   DROPZONE HOVER
   ================================================== */

[data-testid="stFileUploaderDropzone"]:hover {

    background-color: #ffffff !important;

    border-color: #94a3b8 !important;

    box-shadow:
        0 4px 12px rgba(15, 23, 42, 0.06) !important;
}


/* ==================================================
   UPLOAD INSTRUCTION
   ================================================== */

[data-testid="stFileUploaderDropzoneInstructions"] {

    color: #111827 !important;
}


[data-testid="stFileUploaderDropzoneInstructions"] * {

    color: #111827 !important;
}


/* ==================================================
   UPLOAD LIMIT / SIZE TEXT
   ================================================== */

[data-testid="stFileUploaderDropzone"] small {

    color: #64748b !important;

    opacity: 1 !important;
}


[data-testid="stFileUploaderDropzone"] small * {

    color: #64748b !important;

    opacity: 1 !important;
}


/* ==================================================
   UPLOAD BUTTON
   ================================================== */

[data-testid="stFileUploaderDropzone"] button {

    background-color: #000000 !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 8px !important;

    padding: 10px 18px !important;

    font-size: 14px !important;

    font-weight: 600 !important;

    transition:
        background-color 0.2s ease,
        transform 0.2s ease !important;
}


/* ==================================================
   UPLOAD BUTTON TEXT
   ================================================== */

[data-testid="stFileUploaderDropzone"] button span,
[data-testid="stFileUploaderDropzone"] button p {

    color: #ffffff !important;
}


/* ==================================================
   UPLOAD BUTTON HOVER
   ================================================== */

[data-testid="stFileUploaderDropzone"] button:hover {

    background-color: #1f1f1f !important;

    transform: translateY(-1px);
}


/* ==================================================
   UPLOADED FILE CARD
   ================================================== */

[data-testid="stFileUploaderFile"] {

    background-color: #ffffff !important;

    border: 1px solid #dbe2ea !important;

    border-radius: 12px !important;

    padding: 10px 12px !important;

    margin-top: 10px !important;

    box-shadow:
        0 2px 8px rgba(15, 23, 42, 0.06) !important;

    transition:
        box-shadow 0.2s ease,
        border-color 0.2s ease !important;
}


/* ==================================================
   UPLOADED FILE CARD HOVER
   ================================================== */

[data-testid="stFileUploaderFile"]:hover {

    border-color: #cbd5e1 !important;

    box-shadow:
        0 4px 12px rgba(15, 23, 42, 0.09) !important;
}


/* ==================================================
   UPLOADED FILE NAME
   ================================================== */

/* This is the important fix */

[data-testid="stFileUploaderFile"] span {

    color: #1f2937 !important;

    font-size: 13px !important;

    font-weight: 600 !important;
}


/* Nested text */

[data-testid="stFileUploaderFile"] span * {

    color: #1f2937 !important;
}


/* ==================================================
   UPLOADED FILE SIZE
   ================================================== */

[data-testid="stFileUploaderFile"] small {

    color: #64748b !important;

    font-size: 12px !important;

    opacity: 1 !important;
}


[data-testid="stFileUploaderFile"] small * {

    color: #64748b !important;

    opacity: 1 !important;
}


/* ==================================================
   UPLOADED FILE ICON
   ================================================== */

[data-testid="stFileUploaderFile"] svg {

    color: #334155 !important;
}


/* ==================================================
   REMOVE FILE BUTTON
   ================================================== */

[data-testid="stFileUploaderFile"] button {

    background-color: #f1f5f9 !important;

    color: #334155 !important;

    border: none !important;

    border-radius: 8px !important;

    width: 30px !important;

    height: 30px !important;

    padding: 0 !important;

    transition:
        background-color 0.2s ease !important;
}


/* Remove button icon */

[data-testid="stFileUploaderFile"] button svg {

    color: #334155 !important;
}


/* ==================================================
   REMOVE BUTTON HOVER
   ================================================== */

[data-testid="stFileUploaderFile"] button:hover {

    background-color: #e2e8f0 !important;
}


/* ==================================================
   SIDEBAR DIVIDER
   ================================================== */

[data-testid="stSidebar"] hr {

    border: none !important;

    border-top: 1px solid #263244 !important;

    margin-top: 24px !important;

    margin-bottom: 24px !important;
}


/* ==================================================
   SIDEBAR INFO
   ================================================== */

.sidebar-info {

    margin-top: 22px;

    padding-top: 20px;

    border-top: 1px solid #263244;
}


/* ==================================================
   INFO HEADING
   ================================================== */

.info-heading {

    color: #ffffff !important;

    font-size: 14px;

    font-weight: 600;

    margin-bottom: 7px;
}


/* ==================================================
   INFO TEXT
   ================================================== */

.info-text {

    color: #9ca3af !important;

    font-size: 13px;
}


/* ==================================================
   ANALYSIS ITEMS
   ================================================== */

.analysis-item {

    display: flex;

    align-items: center;

    gap: 9px;

    color: #cbd5e1 !important;

    font-size: 13px;

    margin-top: 9px;
}


/* Check mark */

.analysis-item span:first-child {

    color: #94a3b8 !important;

    font-size: 12px;

    font-weight: 700;
}

/* ==================================================
   MAIN HEADER
   ================================================== */

.st-key-header_box {
    background-color: #111827;
    border-radius: 16px;
    padding: 28px 34px;
    margin-bottom: 30px;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.12);
}


/* Header title */

.st-key-header_box h1 {
    color: #ffffff !important;
    font-size: 34px !important;
    font-weight: 700 !important;
    margin: 0 !important;
}


/* Header subtitle */

.st-key-header_box p {
    color: #cbd5e1 !important;
    font-size: 15px !important;
    font-weight: 400 !important;
    margin-top: 8px !important;
}


/* ==================================================
   SECTION HEADINGS
   ================================================== */

h2 {
    color: #111827 !important;
    font-weight: 700 !important;
}

h3 {
    color: #111827 !important;
    font-weight: 700 !important;
}


/* ==================================================
   DATASET OVERVIEW
   ================================================== */

.overview-title {
    font-size: 24px;
    font-weight: 700;
    color: #111827;
    margin-top: 10px;
    margin-bottom: 20px;
}


/* ==================================================
   METRIC CARDS
   ================================================== */

.metric-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 22px 24px;
    min-height: 125px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
    transition: all 0.2s ease;
    margin-bottom: 10px;
}


/* Card hover */

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.09);
}


/* Metric title */

.metric-title {
    color: #64748b;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 12px;
}


/* Metric value */

.metric-value {
    color: #111827;
    font-size: 30px;
    font-weight: 700;
    line-height: 1;
}


/* ==================================================
   TABS CONTAINER
   ================================================== */

/* ==================================================
   TABS CONTAINER
   ================================================== */

/* ==================================================
   STREAMLIT TABS - CUSTOM STYLE
   ================================================== */

/* Main tabs container */
.stTabs {
    margin-top: 28px !important;
}


/* ==================================================
   TAB LIST
   ================================================== */

.stTabs [data-baseweb="tab-list"] {
    display: flex !important;
    align-items: center !important;

    gap: 2px !important;

    background: #ffffff !important;

    padding: 4px !important;

    border: 1px solid #e5e7eb !important;

    border-radius: 10px !important;

    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04) !important;
}


/* ==================================================
   INDIVIDUAL TAB
   ================================================== */

.stTabs [data-baseweb="tab"] {
    position: relative !important;

    height: 40px !important;

    padding: 0 18px !important;

    background: transparent !important;

    color: #64748b !important;

    border: none !important;

    border-radius: 7px !important;

    font-size: 14px !important;

    font-weight: 500 !important;
}


/* ==================================================
   TAB TEXT
   ================================================== */

.stTabs [data-baseweb="tab"] p,
.stTabs [data-baseweb="tab"] span {
    color: #64748b !important;
}


/* ==================================================
   HOVER
   ================================================== */

.stTabs [data-baseweb="tab"]:hover {
    background: #f8fafc !important;
}

.stTabs [data-baseweb="tab"]:hover p,
.stTabs [data-baseweb="tab"]:hover span {
    color: #111827 !important;
}


/* ==================================================
   ACTIVE TAB
   ================================================== */

.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background: #ffffff !important;

    color: #111827 !important;

    font-weight: 600 !important;
}


.stTabs [data-baseweb="tab"][aria-selected="true"] p,
.stTabs [data-baseweb="tab"][aria-selected="true"] span {
    color: #111827 !important;

    font-weight: 600 !important;
}


/* ==================================================
   IMPORTANT:
   STREAMLIT REAL TAB HIGHLIGHT
   ================================================== */

.stTabs [data-baseweb="tab-highlight"] {
    background-color: #111827 !important;

    height: 2px !important;

    border-radius: 2px !important;
}


/* ==================================================
   FORCE ANY RED TAB HIGHLIGHT TO BLACK
   ================================================== */

.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-highlight"] *,
.stTabs div[role="tablist"] [data-baseweb="tab-highlight"] {
    background-color: #111827 !important;

    border-color: #111827 !important;

    box-shadow: none !important;
}


/* ==================================================
   REMOVE OUR PREVIOUS PSEUDO UNDERLINE
   ================================================== */

.stTabs [data-baseweb="tab"][aria-selected="true"]::after {
    display: none !important;

    content: none !important;
}


/* ==================================================
   TAB PANEL
   ================================================== */

.stTabs [data-baseweb="tab-panel"] {
    padding-top: 12px !important;
}
/* ==================================================
   CAPTION
   ================================================== */

[data-testid="stCaptionContainer"] {
    color: #64748b !important;
    font-size: 13px !important;
}


/* ==================================================
   DATAFRAME
   ================================================== */

[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid #e5e7eb !important;
}


/* ==================================================
   ALERTS
   ================================================== */

[data-testid="stAlert"] {
    border-radius: 12px !important;
}


/* ==================================================
   SUCCESS MESSAGE
   ================================================== */

[data-testid="stAlert"][data-baseweb="notification"] {
    margin-bottom: 22px;
}


/* ==================================================
   EMPTY STATE CARDS
   ================================================== */

.feature-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 20px;
    min-height: 130px;
    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.05);
}


/* Feature heading */

.feature-card h3 {
    font-size: 17px;
    margin-bottom: 8px;
}


/* Feature text */

.feature-card p {
    color: #64748b;
    font-size: 13px;
    line-height: 1.5;
}


/* ==================================================
   FOOTER
   ================================================== */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    margin-top: 45px;
    padding-top: 20px;
    border-top: 1px solid #e5e7eb;
}


/* ==================================================
   MOBILE
   ================================================== */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .st-key-header_box {
        padding: 22px;
    }

    .st-key-header_box h1 {
        font-size: 28px !important;
    }

    .metric-card {
        min-height: 110px;
    }

}

</style>
""", unsafe_allow_html=True)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">Data Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'Upload a CSV file to analyze your data.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Upload CSV")

    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown(
        """
        **Supported file**

        CSV files only

        **Analysis includes**

        • Data preview  
        • Statistics  
        • Data types  
        • Missing values
        """
    )


# ==================================================
# MAIN HEADER
# ==================================================

with st.container(key="header_box"):

    st.title("CSV Data Explorer")

    st.write(
        "Upload a CSV file and instantly understand your dataset."
    )


# ==================================================
# NO FILE SELECTED
# ==================================================

if uploaded_file is None:

    st.markdown(
        '<div class="overview-title">What you can explore</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4, gap="medium")


    with col1:

        st.markdown(
            """
            <div class="feature-card">
                <h3>Data Preview</h3>
                <p>
                    View and explore your CSV data in a clean table.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            """
            <div class="feature-card">
                <h3>Statistics</h3>
                <p>
                    Understand numeric data using statistical summaries.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            """
            <div class="feature-card">
                <h3>Data Types</h3>
                <p>
                    Inspect the data type and unique values of each column.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            """
            <div class="feature-card">
                <h3>Missing Values</h3>
                <p>
                    Identify missing or incomplete data in your dataset.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==================================================
# CSV UPLOADED
# ==================================================

else:

    try:

        # ==================================================
        # READ CSV
        # ==================================================

        df = pd.read_csv(uploaded_file)


        # ==================================================
        # CLEAN COLUMN NAMES
        # ==================================================

        df.columns = df.columns.str.strip()


        # ==================================================
        # DATA INFORMATION
        # ==================================================

        rows = df.shape[0]

        cols = df.shape[1]

        missing_values = int(
            df.isnull().sum().sum()
        )

        numeric_columns = len(
            df.select_dtypes(
                include="number"
            ).columns
        )


        # ==================================================
        # SUCCESS MESSAGE
        # ==================================================

        st.success(
            f"Successfully loaded {uploaded_file.name}"
        )


        # ==================================================
        # DATASET OVERVIEW TITLE
        # ==================================================

        st.markdown(
            '<div class="overview-title">Dataset Overview</div>',
            unsafe_allow_html=True
        )


        # ==================================================
        # METRIC CARDS
        # ==================================================

        col1, col2, col3, col4 = st.columns(
            4,
            gap="medium"
        )


        # ==================================================
        # CARD 1
        # ==================================================

        with col1:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        Total Rows
                    </div>
                    <div class="metric-value">
                        {rows:,}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ==================================================
        # CARD 2
        # ==================================================

        with col2:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        Total Columns
                    </div>
                    <div class="metric-value">
                        {cols}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ==================================================
        # CARD 3
        # ==================================================

        with col3:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        Missing Values
                    </div>
                    <div class="metric-value">
                        {missing_values:,}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ==================================================
        # CARD 4
        # ==================================================

        with col4:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        Numeric Columns
                    </div>
                    <div class="metric-value">
                        {numeric_columns}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ==================================================
        # TABS
        # ==================================================

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "Data Preview",
                "Statistics",
                "Data Types",
                "Missing Values"
            ]
        )


        # ==================================================
        # TAB 1 - DATA PREVIEW
        # ==================================================

        with tab1:

            st.markdown(
                '<div class="tab-content-title">'
                'Data Preview'
                '</div>',
                unsafe_allow_html=True
            )

            st.caption(
                f"Showing {rows:,} rows and {cols} columns"
            )

            st.dataframe(
                df,
                use_container_width=True,
                height=500,
                hide_index=True
            )


        # ==================================================
        # TAB 2 - STATISTICS
        # ==================================================

        with tab2:

            st.markdown(
                '<div class="tab-content-title">'
                'Statistical Summary'
                '</div>',
                unsafe_allow_html=True
            )

            numeric_df = df.select_dtypes(
                include="number"
            )

            if not numeric_df.empty:

                statistics = numeric_df.describe().T

                statistics = statistics.round(2)

                st.dataframe(
                    statistics,
                    use_container_width=True
                )

            else:

                st.info(
                    "No numeric columns were found in this CSV."
                )


        # ==================================================
        # TAB 3 - DATA TYPES
        # ==================================================

        with tab3:

            st.markdown(
                '<div class="tab-content-title">'
                'Column Information'
                '</div>',
                unsafe_allow_html=True
            )

            dtype_df = pd.DataFrame(
                {
                    "Column": df.columns,

                    "Data Type":
                        df.dtypes.astype(str).values,

                    "Non-Null Values":
                        df.notnull().sum().values,

                    "Unique Values":
                        df.nunique().values
                }
            )

            st.dataframe(
                dtype_df,
                use_container_width=True,
                hide_index=True
            )


        # ==================================================
        # TAB 4 - MISSING VALUES
        # ==================================================

        with tab4:

            st.markdown(
                '<div class="tab-content-title">'
                'Missing Value Analysis'
                '</div>',
                unsafe_allow_html=True
            )

            missing_df = pd.DataFrame(
                {
                    "Column": df.columns,

                    "Missing Values":
                        df.isnull().sum().values,

                    "Missing %":
                        (
                            df.isnull().mean() * 100
                        ).round(2).values
                }
            )

            missing_df = missing_df[
                missing_df["Missing Values"] > 0
            ]

            if not missing_df.empty:

                st.dataframe(
                    missing_df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.success(
                    "No missing values found in this dataset."
                )


    # ==================================================
    # ERROR HANDLING
    # ==================================================

    except Exception as e:

        st.error(
            "Unable to read this CSV file."
        )

        st.warning(
            f"Error details: {e}"
        )


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div class="footer">
        CSV Data Explorer | Built with Python, Pandas and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)