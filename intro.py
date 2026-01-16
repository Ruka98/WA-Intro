# intro.py
# WA+ Water Accounting Framework (IWMI) — Intro / Welcome window
# - Overview & Workflow refined for both non-technical and technical users
# - Methodology shown as flowcharts + concise details
# - Data Sources tab with authoritative links
# - References & Credits tab
# - Uses QTextBrowser (links work), styled, scrollable

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QScrollArea, QTabWidget, QTextBrowser
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class IntroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WA+ Water Accounting Framework — International Water Management Institute (IWMI)")
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
        tab = QWidget(); v = QVBoxLayout()
        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        content = QWidget(); cv = QVBoxLayout()

        w = self._browser(self._methodology_flowcharts_html())
        cv.addWidget(w)
        content.setLayout(cv)
        scroll.setWidget(content)
        v.addWidget(scroll)
        tab.setLayout(v)
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
            <b>For non-technical users:</b> WA+ is like a financial account for water — tracking each inflow,
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
            <li><b>Sheet 1 — Resource Base:</b> Precipitation & inflows, outflows, ΔStorage</li>
            <li><b>Sheet 2 — Evapotranspiration (Use):</b> ETa by land use; beneficial vs. non-beneficial</li>
        </ul>
        """

    def _workflow_html(self) -> str:
        return """
        <h2 style="color:#2E86C1;">WA+ Workflow — End-to-End</h2>
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

    def _methodology_flowcharts_html(self) -> str:
        return """
        <h2 style="color:#2E86C1;">Methodology</h2>
        <p>WA+ is a robust framework that harnesses the potential of publicly available remote sensing data to assess water resources and their consumption. Its reliance on such data is particularly beneficial in data scarce areas and transboundary basins. A significant benefit of WA+ lies in its incorporation of land use classification into water resource assessments, promoting a holistic approach to land and water management. This integration is crucial for sustaining food production amidst a changing climate, especially in regions where water is scarce. Notably, WA+ application has predominantly centered on monitoring water consumption in irrigated agriculture.</p>

        <p>The WA+ approach builds on a simplified water balance equation for a basin (Karimi et al., 2013):</p>

        <div style="background:#F8F9F9; padding:10px; margin:10px 0; border-left:4px solid #2874A6;">
            <p style="text-align:center; font-weight:bold;">ΔS/Δt = P - ET - Q<sub>out</sub> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (1)</p>
            <p style="font-size:12px;">Where:<br>
            ΔS is the change in storage<br>
            Δt is the change in time<br>
            P is precipitation (mm/year or m³/year)<br>
            ET is total actual evapotranspiration (mm/year or m³/year)<br>
            Q<sub>out</sub> is total surface water outflow (mm/year or m³/year)</p>
        </div>

        <p>To utilize the WA+ approach for water budget reporting in Jordan, it is important to account for all water users, other than irrigation, and their return flows into equation 1. Also, in Jordan, man-made inflows and outflows of great importance especially in heavily populated basins (Amdar et al., 2024). Therefore, an updated water balance incorporating various sectoral water consumption in addition to inflow and outflows is proposed (Amdar et al., 2024). Hence, equation (2) represents the updated WA+ water balance equation in the context of Jordan. This modification will further be refined following detailed discussions and consultations with the WEC and MWI team to ensure complete understanding and consensus of the customized framework for Jordan.</p>

        <div style="background:#F8F9F9; padding:10px; margin:10px 0; border-left:4px solid #2874A6;">
            <p style="text-align:center; font-weight:bold;">ΔS/Δt = (P + Q<sub>in</sub>) - (ET + CW<sub>sec</sub> + Q<sub>WWT</sub> + Q<sub>re</sub> + Q<sub>natural</sub>) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (2)</p>
            <p style="font-size:12px;">Where:<br>
            P is the total precipitation (Mm³/year)<br>
            ET is the total actual evapotranspiration (Mm³/year)<br>
            Q<sub>in</sub> is the total inflows into the basin consisting of both surface water inflows and any other inter-basin transfers (Mm³/year)<br>
            Q<sub>re</sub> is the total recharge to groundwater from precipitation and return flow (Mm³/year)<br>
            Q<sub>WWT</sub> is the total treated waste water that is returned to the river system after treatment. This could be from domestic, industry and tourism sectors (Mm³/year)<br>
            Q<sub>natural</sub> is the naturalized streamflow from the basin (Mm³/year)<br>
            CW<sub>sec</sub> is the total non-irrigated water use/consumption (ie water that is not returned to the system but is consumed by humans) and is given by:</p>

            <p style="text-align:center; font-weight:bold;">CW<sub>sec</sub> = Supply<sub>domestic</sub> + Supply<sub>industrial</sub> + Supply<sub>livestock</sub> + Supply<sub>tourism</sub> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (3)</p>

            <p style="font-size:12px;">Where:<br>
            Supply<sub>domestic</sub> is the water supply for the domestic sector (Mm³/year)<br>
            Supply<sub>industrial</sub> is the water supply for the industrial sector (Mm³/year)<br>
            Supply<sub>livestock</sub> is the water supply for the livestock sector (Mm³/year)<br>
            Supply<sub>tourism</sub> is the water supply for the tourism sector (Mm³/year)</p>
        </div>

        <p>The customized WA+ framework thus takes into account both agricultural and non-irrigated water consumption, water imports and the return of treated wastewater into the basin.</p>

        <style>
          .fc-row { display: flex; flex-wrap: wrap; align-items: center; justify-content: center; margin: 8px 0; }
          .box {
              background:#FFFFFF; border:1px solid #D6DBDF; border-radius:8px;
              padding:10px 14px; margin:6px; min-width:160px; text-align:center;
              box-shadow: 0 1px 2px rgba(0,0,0,0.04);
          }
          .green-box { background:#D5F5E3; border:1px solid #2ECC71; }
          .blue-box { background:#D6EAF8; border:1px solid #3498DB; }
          .beige-box { background:#FCF3CF; border:1px solid #F1C40F; }
          .yellow-box { background:#F9E79F; border:1px solid #F4D03F; }
          .grey-box { background:#E5E7E9; border:1px solid #BDC3C7; }

          .box h4 { margin: 0 0 6px 0; color:#2E86C1; }
          .arrow { font-size: 20px; margin: 0 4px; color:#7F8C8D; }
          .subtle { color:#616A6B; font-size: 12px; margin-top: 6px; }
          .wrap { background:#FDFEFE; border:1px solid #ECF0F1; border-radius:10px; padding:12px; margin-bottom:14px; }
        </style>

        <div class="wrap">
            <h3 style="color:#2874A6; text-align:center;">Customized WA+ Workflow</h3>

            <!-- Row 1: Remote Sensing -->
            <div class="fc-row">
                <div class="box green-box">
                    <h4>WA+ Toolbox</h4>
                    <div class="subtle">Data Download & Spatial Analysis<br>Preprocessing (Resampling, Projecting, Clipping)</div>
                </div>
                <div class="arrow">➜</div>
                <div class="box blue-box">
                    <h4>SM Balance</h4>
                    <div class="subtle">Water Balance Modeling</div>
                </div>
                <div class="arrow">⇄</div>
                <div class="box beige-box">
                    <h4>GR Models</h4>
                    <div class="subtle">Flow Estimation</div>
                </div>
            </div>

            <!-- Row 2: Non-Ag Inputs -->
            <div class="fc-row">
                <div class="box yellow-box">
                    <h4>Non-Agricultural Inputs</h4>
                    <div class="subtle">Water Imports<br>Consumption (Domestic/Tourism/Livestock)<br>Return Wastewater</div>
                </div>
                <div class="arrow">➜</div>
                <div class="box beige-box">
                    <h4>Calibration / Validation</h4>
                    <div class="subtle">Compare with In-situ Data</div>
                </div>
            </div>

            <!-- Connection from Models to Calibration -->
            <div style="text-align:center; color:#7F8C8D; font-size:12px;">(Models also feed into Calibration)</div>

            <!-- Row 3: Output -->
            <div class="fc-row">
                <div class="box beige-box">
                    <h4>Calibration / Validation</h4>
                </div>
                <div class="arrow">➜</div>
                <div class="box yellow-box">
                    <h4>WA Hydroloop</h4>
                    <div class="subtle">Generation of Water Accounts<br>Sheets, Tables, Maps</div>
                </div>
                <div class="arrow">➜</div>
                <div class="box grey-box">
                    <h4>Interpretation</h4>
                    <div class="subtle">Reporting</div>
                </div>
            </div>
        </div>

        <p>During the data preparation step, various remote sensing datasets and tabular data are acquired from different sources. These datasets are then prepared for input and analyzed to select the most representative datasets for the basin of interest. This involves comparison with available in situ data, and any calibration needed to address systematic errors in the remotely sensed data.</p>

        <p>During the second step, the hydrological variability of the basin is characterized by computing various water balance indicators across the watershed using a water balance model. Assessment of the water balance is the core component of the approach; water balance equations are used to describe the flow of water in and out of a system. For the customized WA+ approach for Jordan, the water balance equation is calculated following Equation 4. The change in water storage (ΔS) within a river basin (or sub-basin) is calculated over a monitoring period (Δt) as the difference between the incoming and outgoing water flows. The incoming flows consist of rainfall (precipitation; P) and manmade inflows (Q<sub>in</sub>), and the outgoing flows consist of evapotranspiration (ET), treated waste water returned to stream (Q<sub>wwt</sub>), sectorial water consumption (CW<sub>sec</sub>), and outflows (Q<sub>out</sub>).</p>

        <div style="background:#F8F9F9; padding:10px; margin:10px 0; border-left:4px solid #2874A6;">
            <p style="text-align:center; font-weight:bold;">ΔS/Δt = (P + Q<sub>in</sub>) - (ET + CW<sub>sec</sub> + Q<sub>WWT</sub> + Q<sub>natural</sub>) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (4)</p>
        </div>

        <p>Precipitation and evaporation data were extracted from various remote sensing datasets; data on inflows (water imports for municipal use) and outflows (streamflows from gauge stations used for runoff calibration) were acquired from provided national databases.</p>

        <p>In the fourth step, the water balance results were validated and the model was calibrated by comparing the water balance parameters with in situ data.</p>

        <p>Following this, estimated internal withdrawals, treated waste water and water imports the basin were incorporated into the WA+ toolbox. These were summarized and interpolated from national databases from the governorate level to the basin scale. A full description are provided in section 2.6.1 Basin wide water balance parameters/indicators were then presented for each major land use class (agriculture, urban and natural) through a series of water accounts. The customized WA+ toolbox is summarized in Figure 3 and definitions of the water accounting indicators and a full description of the computation of indicators are provided in Appendix A and B respectively. Briefly, on downloading and gathering remote sensing and tabular data, the observed discharge estimates are combined with the other remote sensing data (precipitation, evapotranspiration, leaf area index etc.) for the soil moisture balance modeling. The soil moisture balance model is a pixel based vertical water balance model for the unsaturated root zone of every pixel that describes the exchanges between land and atmosphere fluxes (i.e. rainfall and evapotranspiration) by partitioning flow into infiltration and surface runoff. The model calculates for each pixel, the ET that is due to rainfall ET, (ET<sub>green</sub>) and that due to additional supply termed incremental ET (ET<sub>blue</sub>) by keeping track of the soil moisture balance (Figure 3). In the final step, non-irrigated water consumption data are combined with the outputs from the soil moisture balance model to generate water accounts at the basin scale.</p>
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
          <li>Karimi, P., Bastiaanssen, W.G.M., et al. (2013). <i>Water Accounting Plus (WA+) — a water accounting procedure for complex river basins.</i></li>
          <li>IWMI / IHE Delft — WA+ manuals, case studies, and methodological notes.</li>
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
        <p>Water Accounting Plus (WA+) Tool — © 2025 IWMI, Water Accounting Team. Licensed under CC BY 4.0.
        For formal publications using WA+ outputs, obtain prior written permission from IWMI as per the included license.</p>
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = IntroWindow()
    win.show()
    sys.exit(app.exec_())
