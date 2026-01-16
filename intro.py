# intro.py
# WA+ Water Accounting Framework (IWMI) - Intro / Welcome window
# - Overview & Workflow refined for both non-technical and technical users
# - Methodology shown as flowcharts + concise details
# - Data Sources tab with authoritative links
# - References & Credits tab
# - Uses QTextBrowser (links work), styled, scrollable

import sys
import os
import base64
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QScrollArea, QTabWidget, QTextBrowser, QSizePolicy
)
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont


class IntroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WA+ Water Accounting Framework - International Water Management Institute (IWMI)")
        self.setGeometry(100, 100, 1000, 780)

        main = QWidget()
        layout = QVBoxLayout()

        # Title
        title = QLabel("Customized Water Accounting Plus Tool for Jordan")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color:#2E86C1; margin-bottom: 16px;")
        layout.addWidget(title)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabBar::tab {
                padding: 8px 12px;
                background: #EAF2F8;
                border: 1px solid #AED6F1;
                border-bottom: none;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background: #2E86C1;
                color: white;
            }
            QTabWidget::pane {
                border: 1px solid #AED6F1;
                top: -1px;
            }
        """)

        self._add_overview_tab()
        self._add_workflow_tab()
        self._add_methodology_tab()  # moved earlier so users see it quickly
        self._add_data_tab()
        self._add_references_tab()

        layout.addWidget(self.tabs)

        # Close
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E86C1;
                color: white;
                border-radius: 6px;
                padding: 10px 22px;
                font-weight: bold;
                min-width: 140px;
            }
            QPushButton:hover { background-color: #2874A6; }
        """)
        layout.addWidget(close_btn, alignment=Qt.AlignCenter)

        main.setLayout(layout)
        self.setCentralWidget(main)

    # ---------- Tabs ----------
    def _add_overview_tab(self):
        tab = QWidget(); v = QVBoxLayout()
        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        content = QWidget(); cv = QVBoxLayout()

        w = self._browser(self._overview_html())
        cv.addWidget(w)
        content.setLayout(cv)
        scroll.setWidget(content)
        v.addWidget(scroll)
        tab.setLayout(v)
        self.tabs.addTab(tab, "Overview")

    def _add_workflow_tab(self):
        tab = QWidget(); v = QVBoxLayout()
        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        content = QWidget(); cv = QVBoxLayout()

        w = self._browser(self._workflow_html())
        cv.addWidget(w)
        content.setLayout(cv)
        scroll.setWidget(content)
        v.addWidget(scroll)
        tab.setLayout(v)
        self.tabs.addTab(tab, "Workflow")

    def _add_methodology_tab(self):
        tab = QWidget()
        v_layout = QVBoxLayout()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        # Create a single seamless content widget with white background
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: white;")
        content_layout = QVBoxLayout()
        # Add some padding around the edges
        content_layout.setContentsMargins(10, 10, 10, 10)

        # Part 1: Text content before the flowchart
        # Use QLabel to ensure it expands fully without internal scrollbars
        lbl_part1 = QLabel(self._methodology_html_part1())
        lbl_part1.setWordWrap(True)
        lbl_part1.setOpenExternalLinks(True)
        lbl_part1.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)
        lbl_part1.setStyleSheet("border: none; padding: 14px;")
        content_layout.addWidget(lbl_part1)

        # Part 2: The flowchart SVG image
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(base_dir, "flowchart.svg")
        svg_widget = QSvgWidget(img_path)
        # Fix size to fit comfortably within the 1000px window width (approx 960 viewable)
        svg_widget.setFixedSize(900, 600)
        content_layout.addWidget(svg_widget, alignment=Qt.AlignCenter)

        # Part 3: Text content after the flowchart (Caption + Text)
        lbl_part2 = QLabel(self._methodology_html_part2())
        lbl_part2.setWordWrap(True)
        lbl_part2.setOpenExternalLinks(True)
        lbl_part2.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)
        lbl_part2.setStyleSheet("border: none; padding: 14px;")
        content_layout.addWidget(lbl_part2)

        # Add stretch to push content up if needed (though content is long enough)
        content_layout.addStretch()

        content_widget.setLayout(content_layout)
        scroll.setWidget(content_widget)
        v_layout.addWidget(scroll)
        tab.setLayout(v_layout)
        self.tabs.addTab(tab, "Methodology (Flowcharts)")

    def _add_data_tab(self):
        tab = QWidget(); v = QVBoxLayout()
        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        content = QWidget(); cv = QVBoxLayout()

        w = self._browser(self._data_html())
        cv.addWidget(w)
        content.setLayout(cv)
        scroll.setWidget(content)
        v.addWidget(scroll)
        tab.setLayout(v)
        self.tabs.addTab(tab, "Data Sources")

    def _add_references_tab(self):
        tab = QWidget(); v = QVBoxLayout()
        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        content = QWidget(); cv = QVBoxLayout()

        w = self._browser(self._references_html())
        cv.addWidget(w)
        content.setLayout(cv)
        scroll.setWidget(content)
        v.addWidget(scroll)
        tab.setLayout(v)
        self.tabs.addTab(tab, "References & Credits")

    # ---------- Helpers ----------
    def _browser(self, html: str) -> QTextBrowser:
        b = QTextBrowser()
        b.setOpenExternalLinks(True)
        b.setStyleSheet("QTextBrowser { background:white; border:none; padding:14px; }")
        b.setHtml(html)
        return b

    # ---------- Content ----------
    def _overview_html(self) -> str:
        return """
        <h2 style="color:#2E86C1;">Introduction</h2>
        <p>Increasing water scarcity is an entrenched problem that faces Jordan. The country is naturally characterized by an arid to semi-arid climate. Water scarcity is compounded by population growth and increasing demands on limited water resources. Climate change is anticipated to reduce long-term conventional water resources (Ministry of Environment, 2021). The combined impact of these factors will likely affect all human activities and the country's economic development. The Water Efficiency and Conservation (WEC) Activity contributes to USAID/Jordan's Country Development Cooperation Strategy's (CDC: 2020-2025) five-year goals of supporting Jordan to advance its stability, prosperity, and self-reliance by spurring including private sector-led economic growth, improving water security, strengthening accountable governance, fostering a healthy, well-educated population, and enhancing the agency and leadership of women and youth. The International Water Management Institute (IWMI) is non-profit research for development organization headquartered in Colombo, Sri Lanka, with offices throughout Asia, and Africa, including a regional office for the MENA region in Egypt with a team in Jordan. IWMI is a member of the CGIAR System of international agricultural research centers, a global research partnership for a food-secure future dedicated to reducing poverty, enhancing food and nutrition security, and improving natural resources. IWMI's vision is a water-secure world, and our mission is to provide water solutions for sustainable, climate-resilient development. IWMI has conducted active research programs in Jordan since the 2000s and the latest contributions in Jordan included Monitoring & Evaluation (M&E) inputs to the USAID’s Water Innovation Technologies (WIT) project, leading the field-scale monitoring and evaluation of water savings generated from adopting water-saving technologies across agriculture and domestic sectors and communal water use.</p>

        <h2 style="color:#2E86C1;">What is WA+?</h2>
        <p><b>Water Accounting Plus (WA+)</b> is a standardized framework developed by the
        International Water Management Institute (IWMI) and partners to measure, monitor,
        and communicate how water is <i>available</i>, <i>used</i>, and <i>shared</i> in river basins.</p>

        <div style="background:#EBF5FB; padding:12px; border-left:5px solid #2E86C1; margin:12px 0;">
            <p style="margin:0;">
            <b>For non-technical users:</b> WA+ is like a financial account for water - tracking each inflow,
            outflow, and change in storage to build trust and support fair allocation.<br><br>
            <b>For technical users:</b> WA+ provides consistent definitions, spatially explicit datasets, and
            reproducible calculations for basin-scale auditing, with options to validate against independent observations.
            </p>
        </div>

        <h3 style="color:#2874A6;">What problems does WA+ solve?</h3>
        <ul>
          <li><b>Transparency:</b> A clear, shared picture of availability, use, and trends</li>
          <li><b>Comparability:</b> Standard “Sheets” enable apples-to-apples comparison across basins/years</li>
          <li><b>Decision support:</b> Identifies scarcity, inefficiency, and trade-offs for planning & policy</li>
        </ul>

        <h3 style="color:#2874A6;">Core concepts</h3>
        <ul>
          <li><b>Water balance:</b> Inflows = Outflows ± ΔStorage (soil, groundwater, surface water)</li>
          <li><b>Consumptive use (ETa):</b> Water actually consumed by vegetation, open water, and urban areas</li>
          <li><b>Beneficial vs. non-beneficial consumption:</b> Productive transpiration vs. losses like bare-soil evaporation</li>
          <li><b>Green vs. Blue water:</b> Rain-fed consumption vs. managed supply (e.g., irrigation)</li>
        </ul>

        <h3 style="color:#2874A6;">WA+ Sheets (standard outputs)</h3>
        <ul>
            <li><b>Sheet 1 - Resource Base:</b> Precipitation & inflows, outflows, ΔStorage</li>
            <li><b>Sheet 2 - Evapotranspiration (Use):</b> ETa by land use; beneficial vs. non-beneficial</li>
        </ul>
        """

    def _workflow_html(self) -> str:
        return """
        <h2 style="color:#2E86C1;">WA+ Workflow - End-to-End</h2>
        <p>WA+ turns heterogeneous data into standard accounts through a transparent, repeatable process.</p>

        <div style="background:#F8F9F9; padding:14px; border:1px solid #E5E7E9; border-radius:8px;">
          <h3 style="color:#2874A6; margin-top:0;">High-level stages</h3>
          <ol>
            <li><b>Define the Basin & Period:</b> AOI/basin boundary, reporting year(s) or seasons</li>
            <li><b>Acquire Inputs:</b> Precipitation, ET, vegetation, DEM, soil moisture, surface water, land cover</li>
            <li><b>Pre-process & Harmonize:</b> Reprojection, resampling, QA/QC, gap-filling; convert to common grids (NetCDF)</li>
            <li><b>Compute Fluxes & Stores:</b> ETa, runoff proxies, ΔStorage; decompose ET (T/E) and green/blue shares</li>
            <li><b>Stratify by Land Use:</b> Protected / Utilized(Modified) / Managed water-use classes</li>
            <li><b>Assemble WA+ Sheets:</b> Resource base, ET use, productivity, withdrawals, surface water, groundwater</li>
            <li><b>Validate & Review:</b> Cross-check ΔS with GRACE; compare flows with gauges; stakeholder review</li>
            <li><b>Report & Share:</b> Maps, charts, time series, and sheet summaries</li>
          </ol>
        </div>

        <p style="margin-top:12px;"><b>Tip for users:</b> In this app, the <i>NetCDF</i> step standardizes inputs so downstream
        analysis and reporting are consistent and reproducible.</p>
        """

    def _methodology_html_part1(self) -> str:
        return """
        <h2 style="color:#2E86C1;">Customized WA+ Analytical Framework for Jordan</h2>
        <p>WA+ is a robust framework that harnesses the potential of publicly available remote sensing data to assess water resources and their consumption. Its reliance on such data is particularly beneficial in data scarce areas and transboundary basins. A significant benefit of WA+ lies in its incorporation of land use classification into water resource assessments, promoting a holistic approach to land and water management. This integration is crucial for sustaining food production amidst a changing climate, especially in regions where water is scarce. Notably, WA+ application has predominantly centered on monitoring water consumption in irrigated agriculture.</p>

        <p>The WA+ approach builds on a simplified water balance equation for a basin (Karimi et al., 2013):</p>

        <div style="background:#F8F9F9; padding:10px; margin:10px 0; border-left:4px solid #2874A6;">
            <p style="text-align:center; font-family:'Times New Roman', serif; font-size:16px;">
            <i>&Delta;S</i>/<i>&Delta;t</i> = <i>P</i> - <i>ET</i> - <i>Q<sub>out</sub></i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (1)
            </p>
            <p style="font-size:14px; margin-left:20px;">
            Where:<br>
            <i>&Delta;S</i> is the change in storage<br>
            <i>&Delta;t</i> is the change in time<br>
            <i>P</i> is precipitation (mm/year or m<sup>3</sup>/year)<br>
            <i>ET</i> is total actual evapotranspiration (mm/year or m<sup>3</sup>/year)<br>
            <i>Q<sub>out</sub></i> is total surface water outflow (mm/year or m<sup>3</sup>/year)
            </p>
        </div>

        <p>To utilize the WA+ approach for water budget reporting in Jordan, it is important to account for all water users, other than irrigation, and their return flows into equation 1. Also, in Jordan, man-made inflows and outflows of great importance especially in heavily populated basins (Amdar et al., 2024). Therefore, an updated water balance incorporating various sectoral water consumption in addition to inflow and outflows is proposed (Amdar et al., 2024). Hence, equation (2) represents the updated WA+ water balance equation in the context of Jordan. This modification will further be refined following detailed discussions and consultations with the WEC and MWI team to ensure complete understanding and consensus of the customized framework for Jordan.</p>

        <div style="background:#F8F9F9; padding:10px; margin:10px 0; border-left:4px solid #2874A6;">
            <p style="text-align:center; font-family:'Times New Roman', serif; font-size:16px;">
            <i>&Delta;S</i>/<i>&Delta;t</i> = (<i>P</i> + <i>Q<sub>in</sub></i>) - (<i>ET</i> + <i>CW<sub>sec</sub></i> + <i>Q<sub>WWT</sub></i> + <i>Q<sub>re</sub></i> + <i>Q<sub>natural</sub></i>) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (2)
            </p>
            <p style="font-size:14px; margin-left:20px;">
            Where:<br>
            <i>P</i> is the total precipitation (Mm<sup>3</sup>/year)<br>
            <i>ET</i> is the total actual evapotranspiration (Mm<sup>3</sup>/year)<br>
            <i>Q<sub>in</sub></i> is the total inflows into the basin consisting of both surface water inflows and any other inter-basin transfers (Mm<sup>3</sup>/year)<br>
            <i>Q<sub>re</sub></i> is the total recharge to groundwater from precipitation and return flow (Mm<sup>3</sup>/year)<br>
            <i>Q<sub>WWT</sub></i> is the total treated waste water that is returned to the river system after treatment. This could be from domestic, industry and tourism sectors (Mm<sup>3</sup>/year)<br>
            <i>Q<sub>natural</sub></i> is the naturalized streamflow from the basin (Mm<sup>3</sup>/year)<br>
            <i>CW<sub>sec</sub></i> is the total non-irrigated water use/consumption (ie water that is not returned to the system but is consumed by humans) and is given by:
            </p>

            <p style="text-align:center; font-family:'Times New Roman', serif; font-size:16px;">
            <i>CW<sub>sec</sub></i> = <i>Supply<sub>domestic</sub></i> + <i>Supply<sub>industrial</sub></i> + <i>Supply<sub>livestock</sub></i> + <i>Supply<sub>tourism</sub></i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (3)
            </p>

            <p style="font-size:14px; margin-left:20px;">
            Where:<br>
            <i>Supply<sub>domestic</sub></i> is the water supply for the domestic sector (Mm<sup>3</sup>/year)<br>
            <i>Supply<sub>industrial</sub></i> is the water supply for the industrial sector (Mm<sup>3</sup>/year)<br>
            <i>Supply<sub>livestock</sub></i> is the water supply for the livestock sector (Mm<sup>3</sup>/year)<br>
            <i>Supply<sub>tourism</sub></i> is the water supply for the tourism sector (Mm<sup>3</sup>/year)
            </p>
        </div>

        <p>The customized WA+ framework thus takes into account both agricultural and non-irrigated water consumption, water imports and the return of treated wastewater into the basin.</p>
        """

    def _methodology_html_part2(self) -> str:
        return """
        <div style="text-align:center; font-weight:bold; margin:10px 0 20px 0; color:#2E86C1;">
            Figure 2. The WA+ toolbox: main processing modules of the customized WA+ Framework for Jordan.
        </div>

        <p>Implementation of the WA+ framework involves automated collection, pre-processing and computation of the water balance for a river basin and its sub-basins through the WA+ toolbox. The customized framework for the Amman Zarqa basin consists of six major steps to calculate and present the water accounts: data download and pre-processing, water balance modeling, calibration/validation of streamflow, estimation of non-agricultural water consumption, generation of water accounts, and interpretation and presentation of results.</p>

        <p>During the data preparation step, various remote sensing datasets and tabular data are acquired from different sources. These datasets are then prepared for input and analyzed to select the most representative datasets for the basin of interest. This involves comparison with available in situ data, and any calibration needed to address systematic errors in the remotely sensed data.</p>

        <p>During the second step, the hydrological variability of the basin is characterized by computing various water balance indicators across the watershed using a water balance model. Assessment of the water balance is the core component of the approach; water balance equations are used to describe the flow of water in and out of a system. For the customized WA+ approach for Jordan, the water balance equation is calculated following Equation 4. The change in water storage (<i>&Delta;S</i>) within a river basin (or sub-basin) is calculated over a monitoring period (<i>&Delta;t</i>) as the difference between the incoming and outgoing water flows. The incoming flows consist of rainfall (precipitation; <i>P</i>) and manmade inflows (<i>Q<sub>in</sub></i>), and the outgoing flows consist of evapotranspiration (<i>ET</i>), treated waste water returned to stream (<i>Q<sub>wwt</sub></i>), sectorial water consumption (<i>CW<sub>sec</sub></i>), and outflows (<i>Q<sub>out</sub></i>).</p>

        <div style="background:#F8F9F9; padding:10px; margin:10px 0; border-left:4px solid #2874A6;">
            <p style="text-align:center; font-family:'Times New Roman', serif; font-size:16px;">
            <i>&Delta;S</i>/<i>&Delta;t</i> = (<i>P</i> + <i>Q<sub>in</sub></i>) - (<i>ET</i> + <i>CW<sub>sec</sub></i> + <i>Q<sub>WWT</sub></i> + <i>Q<sub>natural</sub></i>) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (4)
            </p>
        </div>

        <p>Precipitation and evaporation data were extracted from various remote sensing datasets; data on inflows (water imports for municipal use) and outflows (streamflows from gauge stations used for runoff calibration) were acquired from provided national databases.</p>

        <p>In the fourth step, the water balance results were validated and the model was calibrated by comparing the water balance parameters with in situ data.</p>

        <p>Following this, estimated internal withdrawals, treated waste water and water imports the basin were incorporated into the WA+ toolbox. These were summarized and interpolated from national databases from the governorate level to the basin scale. A full description is provided in section 2.6.1. Basin wide water balance parameters/indicators were then presented for each major land use class (agriculture, urban and natural) through a series of water accounts. The customized WA+ toolbox is summarized in Figure 2 and definitions of the water accounting indicators and a full description of the computation of indicators are provided in Appendix A and B respectively. Briefly, on downloading and gathering remote sensing and tabular data, the observed discharge estimates are combined with the other remote sensing data (precipitation, evapotranspiration, leaf area index etc.) for the soil moisture balance modeling. The soil moisture balance model is a pixel based vertical water balance model for the unsaturated root zone of every pixel that describes the exchanges between land and atmosphere fluxes (i.e. rainfall and evapotranspiration) by partitioning flow into infiltration and surface runoff. The model calculates for each pixel, the ET that is due to rainfall ET (<i>ET<sub>green</sub></i>) and that due to additional supply termed incremental ET (<i>ET<sub>blue</sub></i>) by keeping track of the soil moisture balance (Figure 2). In the final step, non-irrigated water consumption data are combined with the outputs from the soil moisture balance model to generate water accounts at the basin scale.</p>
        """

    def _data_html(self) -> str:
        return """
        <h2 style="color:#2E86C1;">Data Sources Used in WA+</h2>
        <p>WA+ relies on open, global datasets for transparency and repeatability. Key sources include:</p>

        <table border="1" cellspacing="0" cellpadding="8" width="100%" style="border-collapse:collapse;">
          <tr style="background:#EAF2F8;">
            <th width="22%">Variable</th>
            <th width="38%">Dataset (Official Link)</th>
            <th width="40%">Use in WA+</th>
          </tr>
          <tr>
            <td>Precipitation</td>
            <td><a href="https://www.chc.ucsb.edu/data/chirps">CHIRPS</a></td>
            <td>Main rainfall input (inflows to basin water balance)</td>
          </tr>
          <tr style="background:#F9F9F9;">
            <td>Evapotranspiration</td>
            <td><a href="https://earlywarning.usgs.gov/fews/evaporation">SSEBop (USGS/FEWS NET)</a>, MODIS MOD16, GLEAM</td>
            <td>Actual consumptive use (water depletion / ETa)</td>
          </tr>
          <tr>
            <td>Vegetation & Biomass</td>
            <td><a href="https://modis.gsfc.nasa.gov/data/dataprod/mod13.php">MODIS NDVI / LAI</a></td>
            <td>Crop growth, biomass proxies; supports productivity estimates</td>
          </tr>
          <tr style="background:#F9F9F9;">
            <td>Topography (DEM)</td>
            <td><a href="https://lpdaac.usgs.gov/products/nasadem_hgtv001/">SRTM / NASADEM</a></td>
            <td>Basin boundaries, flow routing, sub-basin analysis</td>
          </tr>
          <tr>
            <td>Surface Water</td>
            <td><a href="https://global-surface-water.appspot.com">JRC Global Surface Water</a></td>
            <td>Open-water extent, reservoir & lake dynamics (supports ET/open water & storage)</td>
          </tr>
          <tr style="background:#F9F9F9;">
            <td>Soil Moisture</td>
            <td><a href="https://climate.esa.int/en/projects/soil-moisture/">ESA CCI Soil Moisture</a></td>
            <td>Soil water balance; constrains infiltration/availability</td>
          </tr>
          <tr>
            <td>Total Water Storage / GW</td>
            <td><a href="https://grace.jpl.nasa.gov/data">NASA GRACE / GRACE-FO</a></td>
            <td>Independent check on ΔStorage; groundwater trend signals</td>
          </tr>
          <tr style="background:#F9F9F9;">
            <td>Land Cover / Use</td>
            <td><a href="https://climate.esa.int/en/projects/land-cover/">ESA CCI Land Cover</a></td>
            <td>Stratification of WA+ sheets by land use classes</td>
          </tr>
        </table>

        <p style="margin-top:10px;">
          <b>Notes for practitioners:</b> ET can be multi-sourced (e.g., SSEBop, MOD16, GLEAM) and ensembled for robustness.
          Land-use may combine global layers with national maps (irrigated areas, protected areas, crop masks) for best accuracy.
        </p>
        """

    def _references_html(self) -> str:
        return """
        <h2 style="color:#2E86C1;">References & Credits</h2>
        <p><b>Developed by:</b> Water Accounting Team, International Water Management Institute (IWMI), with partners.</p>

        <h3 style="color:#2874A6;">Key References (selected)</h3>
        <ul>
          <li>Karimi, P., Bastiaanssen, W.G.M., et al. (2013). <i>Water Accounting Plus (WA+) - a water accounting procedure for complex river basins.</i></li>
          <li>IWMI / IHE Delft - WA+ manuals, case studies, and methodological notes.</li>
          <li>ET products documentation (SSEBop, MOD16, GLEAM) and CHIRPS precipitation product notes.</li>
        </ul>

        <h3 style="color:#2874A6;">Official Resources</h3>
        <ul>
          <li><a href="https://www.iwmi.org">International Water Management Institute (IWMI)</a></li>
          <li><a href="https://www.ihe-delft.nl">IHE Delft Institute for Water Education</a></li>
        </ul>

        <h3 style="color:#2874A6;">Data Portals (again)</h3>
        <ul>
          <li><a href="https://www.chc.ucsb.edu/data/chirps">CHIRPS precipitation</a></li>
          <li><a href="https://earlywarning.usgs.gov/fews/evaporation">SSEBop evapotranspiration</a></li>
          <li><a href="https://modis.gsfc.nasa.gov/data/dataprod/mod13.php">MODIS NDVI / LAI</a></li>
          <li><a href="https://lpdaac.usgs.gov/products/nasadem_hgtv001/">SRTM / NASADEM DEM</a></li>
          <li><a href="https://global-surface-water.appspot.com">JRC Global Surface Water</a></li>
          <li><a href="https://climate.esa.int/en/projects/soil-moisture/">ESA CCI Soil Moisture</a></li>
          <li><a href="https://grace.jpl.nasa.gov/data">NASA GRACE / GRACE-FO</a></li>
          <li><a href="https://climate.esa.int/en/projects/land-cover/">ESA CCI Land Cover</a></li>
        </ul>

        <h3 style="color:#2874A6;">Credits & License</h3>
        <p>Water Accounting Plus (WA+) Tool - &copy; 2025 IWMI, Water Accounting Team. Licensed under CC BY 4.0.
        For formal publications using WA+ outputs, obtain prior written permission from IWMI as per the included license.</p>
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = IntroWindow()
    win.show()
    sys.exit(app.exec_())
