from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Electronics for CSE - Easy Solutions", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 11)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(3)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

content = {
    "1. PN Junction Diode": """- A PN junction is formed by joining P-type and N-type semiconductors.
- In forward bias, it conducts; in reverse bias, it blocks current.
- The I-V characteristic shows exponential increase in current in forward bias and a small leakage in reverse bias.""",

    "2. Half-Wave & Full-Wave Rectifiers": """- Half-wave rectifier allows one half of the AC signal.
- Full-wave rectifier uses both halves of the input signal.
- Full-wave has higher efficiency and lower ripple factor.
- Average Output (Half-wave): V_avg = Vm/π; Full-wave: V_avg = 2Vm/π.""",

    "3. Zener Diode & Voltage Regulation": """- Zener diode works in reverse bias and maintains a constant voltage.
- Used in voltage regulation.
- When input voltage exceeds Zener voltage, it conducts and clamps the voltage.""",

    "4. Clipping and Clamping Circuits": """- Clipping: Limits voltage above/below a certain level.
- Clamping: Shifts the signal voltage up/down without changing shape.
- Uses diodes and sometimes DC sources.""",

    "5. BJT and Configurations": """- BJT has three regions: active, saturation, cutoff.
- In CE configuration, it's used for amplification.
- In saturation: acts as a closed switch.
- In cutoff: acts as an open switch.
- Common emitter has high gain, common base has low input resistance, common collector has high input resistance.""",

    "6. Biasing and Amplifiers": """- Biasing sets the Q-point for linear operation.
- Voltage-divider bias is stable.
- Amplifiers increase signal strength.
- Current mirror ensures constant current using two BJTs."""
}

for title, body in content.items():
    pdf.chapter_title(title)
    pdf.chapter_body(body)

pdf.output("Electronics_Easy_Solutions.pdf")
