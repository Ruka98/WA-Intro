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
        title = QLabel("Water Accounting Plus (WA+) Tool")
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
            <li><b>Sheet 3 — Productivity:</b> Biomass/crop output and water productivity</li>
            <li><b>Sheet 4 — Withdrawals:</b> Blue-water abstractions and returns</li>
            <li><b>Sheet 5 — Surface Water:</b> River flows, reservoirs, environmental allocations</li>
            <li><b>Sheet 6 — Groundwater:</b> Recharge, abstraction, long-term storage changes</li>
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
        # Styled flowchart blocks using simple HTML/CSS that QTextBrowser can render
        return """
        <style>
          .fc-row { display: flex; flex-wrap: wrap; align-items: center; justify-content: center; margin: 8px 0; }
          .box {
              background:#FFFFFF; border:1px solid #D6DBDF; border-radius:8px;
              padding:10px 14px; margin:6px; min-width:160px; text-align:center;
              box-shadow: 0 1px 2px rgba(0,0,0,0.04);
          }
          .box h4 { margin: 0 0 6px 0; color:#2E86C1; }
          .arrow { font-size: 20px; margin: 0 4px; color:#7F8C8D; }
          .subtle { color:#616A6B; font-size: 12px; margin-top: 6px; }
          .wrap { background:#FDFEFE; border:1px solid #ECF0F1; border-radius:10px; padding:12px; margin-bottom:14px; }
          .title { color:#2874A6; margin: 6px 0 8px 0; }
          .pill { display:inline-block; background:#EAF2F8; border:1px solid #AED6F1; border-radius:999px; padding:4px 10px; margin:2px; font-size:12px; }
        </style>

        <h2 style="color:#2E86C1;">Methodology — Flowcharts & Details</h2>
        <p>These flowcharts show <b>how WA+</b> converts inputs into audited water accounts. Hover-style effects are not used to keep things light.</p>

        <div class="wrap">
          <h3 class="title">A) Basin Water Balance</h3>
          <div class="fc-row">
            <div class="box"><h4>Precipitation (P)</h4><div class="subtle">CHIRPS</div></div>
            <div class="arrow">➕</div>
            <div class="box"><h4>Upstream Inflows (Q<sub>in</sub>)</h4><div class="subtle">gauges / modeled</div></div>
            <div class="arrow">➕</div>
            <div class="box"><h4>Transfers</h4><div class="subtle">e.g., imports</div></div>
            <div class="arrow">➜</div>
            <div class="box"><h4>Partition</h4><div class="subtle">infiltration / runoff</div></div>
            <div class="arrow">➜</div>
            <div class="box"><h4>Outflows (Q<sub>out</sub>)</h4><div class="subtle">discharge</div></div>
            <div class="arrow">➕</div>
            <div class="box"><h4>ETa</h4><div class="subtle">SSEBop / MOD16 / GLEAM</div></div>
            <div class="arrow">➕/➖</div>
            <div class="box"><h4>ΔStorage</h4><div class="subtle">soil + GW + surface</div></div>
          </div>
          <div class="subtle">Water balance: <b>P + Q<sub>in</sub> ± transfers − (ETa + Q<sub>out</sub>) = ΔS</b></div>
        </div>

        <div class="wrap">
          <h3 class="title">B) ET Decomposition</h3>
          <div class="fc-row">
            <div class="box"><h4>ETa</h4><div class="subtle">actual consumption</div></div>
            <div class="arrow">➜</div>
            <div class="box"><h4>Transpiration (T)</h4><div class="subtle pill">Beneficial</div></div>
            <div class="arrow">➕</div>
            <div class="box"><h4>Soil Evaporation (E<sub>soil</sub>)</h4><div class="subtle pill">Non-beneficial</div></div>
            <div class="arrow">➕</div>
            <div class="box"><h4>Open-Water Evap (E<sub>ow</sub>)</h4><div class="subtle pill">Context</div></div>
            <div class="arrow">➕</div>
            <div class="box"><h4>Interception</h4><div class="subtle pill">Context</div></div>
          </div>
          <div class="subtle">Green vs. Blue split applied to ETa to identify rain-fed vs. managed consumption.</div>
        </div>

        <div class="wrap">
          <h3 class="title">C) Land-Use Stratification</h3>
          <div class="fc-row">
            <div class="box"><h4>Land Cover</h4><div class="subtle">ESA CCI / national</div></div>
            <div class="arrow">➜</div>
            <div class="box"><h4>Protected</h4></div>
            <div class="arrow">➕</div>
            <div class="box"><h4>Utilized / Modified</h4></div>
            <div class="arrow">➕</div>
            <div class="box"><h4>Managed Water Use</h4><div class="subtle">e.g., irrigated</div></div>
          </div>
          <div class="subtle">All WA+ indicators are computed and reported per class for transparency.</div>
        </div>

        <div class="wrap">
          <h3 class="title">D) Productivity Indicators</h3>
          <div class="fc-row">
            <div class="box"><h4>Vegetation Indices</h4><div class="subtle">MODIS NDVI/LAI</div></div>
            <div class="arrow">➜</div>
            <div class="box"><h4>Biomass / Yield</h4><div class="subtle">NPP proxies</div></div>
            <div class="arrow">➗</div>
            <div class="box"><h4>ETa (T-focused)</h4><div class="subtle">beneficial share</div></div>
            <div class="arrow">➜</div>
            <div class="box"><h4>Water Productivity</h4><div class="subtle">kg per m³</div></div>
          </div>
          <div class="subtle">Emphasis on transpiration-driven production for meaningful efficiency metrics.</div>
        </div>

        <div class="wrap">
          <h3 class="title">E) Validation & Review</h3>
          <div class="fc-row">
            <div class="box"><h4>ΔS (from balance)</h4></div>
            <div class="arrow">⇄</div>
            <div class="box"><h4>GRACE / GRACE-FO</h4><div class="subtle">total storage change</div></div>
            <div class="arrow">⇄</div>
            <div class="box"><h4>River Gauges</h4><div class="subtle">Q<sub>out</sub> checks</div></div>
            <div class="arrow">⇄</div>
            <div class="box"><h4>Stakeholder Review</h4><div class="subtle">context & QA</div></div>
          </div>
          <div class="subtle">Iterative improvement ensures credible, decision-ready accounts.</div>
        </div>

        <p class="subtle">Outputs: WA+ Sheets (1–6), maps, charts, and time series for planning, policy, and investment.</p>
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
