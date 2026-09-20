"""
Generator for GAMEKART TYBCA Minor Project Documentation Report (DOCX)
Compliant with the College 10-Point Syllabus Guidelines:
(i) Cover Page
(ii) Minor Project Completion Certificate
(iii) Index
(iv) Introduction
(v) Technology used
(vi) Objectives
(vii) System Flow Chart
(viii) Database Design
(ix) Screen Shots
(x) References
Target Page Count: 25 to 30 pages.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# --- Color Palette ---
COLOR_PRIMARY = RGBColor(27, 54, 93)      # Navy Blue (#1B365D)
COLOR_SECONDARY = RGBColor(44, 82, 130)   # Medium Blue (#2C5282)
COLOR_DARK = RGBColor(30, 41, 59)         # Slate Dark (#1E293B)
COLOR_MUTED = RGBColor(100, 116, 139)     # Slate Muted (#64748B)
COLOR_TEXT = RGBColor(33, 37, 41)         # Dark Gray (#212529)

HEX_PRIMARY = "1B365D"
HEX_SECONDARY = "2C5282"
HEX_LIGHT_BG = "F8FAFC"
HEX_ZEBRA = "F1F5F9"
HEX_BORDER = "CBD5E1"
HEX_CALLOUT_BG = "F0F4F8"

def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color=HEX_BORDER, sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def make_table_header_repeat(table):
    trPr = table.rows[0]._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

def prevent_row_split(table):
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

def add_page_number_to_run(run):
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = COLOR_SECONDARY
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_DARK
    return p

def add_body_p(doc, text, space_after=5):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    run.font.color.rgb = COLOR_TEXT
    return p

def add_bullet_p(doc, text, bold_prefix=None, space_after=4):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_PRIMARY
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    run.font.color.rgb = COLOR_TEXT
    return p

def add_callout(doc, text, title=None):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, HEX_CALLOUT_BG)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=140)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_PRIMARY}"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    
    if title:
        r_t = p.add_run(f"📌 {title}\n")
        r_t.font.name = 'Times New Roman'
        r_t.font.size = Pt(10.5)
        r_t.font.bold = True
        r_t.font.color.rgb = COLOR_PRIMARY
        
    r_body = p.add_run(text)
    r_body.font.name = 'Times New Roman'
    r_body.font.size = Pt(10)
    r_body.font.italic = True
    r_body.font.color.rgb = COLOR_DARK
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def add_figure_image(doc, img_path, caption, width_in=5.6, space_after=6):
    try:
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(2)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_in))
    except Exception as e:
        print(f"Warning: could not add image {img_path}: {e}")
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p_img.add_run(f"[{os.path.basename(img_path)}]")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.italic = True
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(space_after)
    run_cap = p_cap.add_run(caption)
    run_cap.font.name = 'Times New Roman'
    run_cap.font.size = Pt(9.5)
    run_cap.font.italic = True
    run_cap.font.bold = True
    run_cap.font.color.rgb = COLOR_MUTED
    return p_cap

def add_styled_table(doc, headers, data, col_widths=None, font_size=9.5):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table, color=HEX_BORDER, sz="4")
    make_table_header_repeat(table)
    prevent_row_split(table)
    
    hdr_row = table.rows[0]
    for idx, heading in enumerate(headers):
        cell = hdr_row.cells[idx]
        set_cell_background(cell, HEX_PRIMARY)
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(heading)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(font_size)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        if col_widths and idx < len(col_widths):
            cell.width = Inches(col_widths[idx])
            
    for row_idx, row_data in enumerate(data):
        row = table.rows[row_idx + 1]
        bg_color = HEX_ZEBRA if (row_idx % 2 == 1) else HEX_LIGHT_BG
        for col_idx, cell_value in enumerate(row_data):
            cell = row.cells[col_idx]
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(str(cell_value))
            run.font.name = 'Times New Roman'
            run.font.size = Pt(font_size)
            run.font.color.rgb = COLOR_TEXT
            if col_widths and col_idx < len(col_widths):
                cell.width = Inches(col_widths[col_idx])
                
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(4)
    return table

def add_code_block(doc, code_str, caption=None):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "1E293B")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    
    run = p.add_run(code_str)
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(226, 232, 240)
    
    if caption:
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(4)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(9.0)
        run_cap.font.italic = True
        run_cap.font.color.rgb = COLOR_MUTED


def build_final_project_documentation():
    output_filename = "GAMEKART_TYBCA_PROJECT_DOCUMENTATION.docx"
    doc = docx.Document()
    
    # Page setup
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        
    # Headers and footers
    section = doc.sections[0]
    header = section.header
    p_hdr = header.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_hdr = p_hdr.add_run("TYBCA Minor Project Documentation | AWD & WFS (2025–2026)")
    r_hdr.font.name = 'Times New Roman'
    r_hdr.font.size = Pt(8.5)
    r_hdr.font.italic = True
    r_hdr.font.color.rgb = COLOR_MUTED
    
    footer = section.footer
    tbl_ftr = footer.add_table(rows=1, cols=2, width=Inches(6.5))
    tbl_ftr.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_left = tbl_ftr.cell(0, 0)
    c_right = tbl_ftr.cell(0, 1)
    
    p_fl = c_left.paragraphs[0]
    p_fl.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_fl = p_fl.add_run("GameKart — Full-Stack E-Commerce Platform")
    r_fl.font.name = 'Times New Roman'
    r_fl.font.size = Pt(8.5)
    r_fl.font.color.rgb = COLOR_MUTED
    
    p_fr = c_right.paragraphs[0]
    p_fr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_fr = p_fr.add_run("Page ")
    r_fr.font.name = 'Times New Roman'
    r_fr.font.size = Pt(8.5)
    r_fr.font.color.rgb = COLOR_MUTED
    add_page_number_to_run(r_fr)

    # =============================================================
    # (i) COVER PAGE
    # =============================================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(10)
    p_inst.paragraph_format.space_after = Pt(4)
    r_inst = p_inst.add_run("DEPARTMENT OF COMPUTER APPLICATIONS\nBACHELOR OF COMPUTER APPLICATIONS (BCA)")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(14)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_PRIMARY
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(2)
    p_sub.paragraph_format.space_after = Pt(24)
    r_sub = p_sub.add_run("TYBCA — SEMESTER V (ACADEMIC YEAR 2025–2026)\nAWD (Advanced Web Development) & WFS (Web Frameworks & Services)")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(11)
    r_sub.font.bold = True
    r_sub.font.color.rgb = COLOR_MUTED
    
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_before = Pt(0)
    p_line.paragraph_format.space_after = Pt(24)
    r_line = p_line.add_run("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    r_line.font.name = 'Times New Roman'
    r_line.font.size = Pt(12)
    r_line.font.color.rgb = COLOR_PRIMARY

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("GAMEKART\nE-COMMERCE GAMING ACCESSORIES & HARDWARE STORE")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(22)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_PRIMARY
    
    p_desc = doc.add_paragraph()
    p_desc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_desc.paragraph_format.space_before = Pt(4)
    p_desc.paragraph_format.space_after = Pt(36)
    r_desc = p_desc.add_run("A Full-Stack Reactive Web Application with Dual Port Micro-Architecture,\nRESTful Web Services, and MongoDB Database Management")
    r_desc.font.name = 'Times New Roman'
    r_desc.font.size = Pt(12)
    r_desc.font.italic = True
    r_desc.font.color.rgb = COLOR_SECONDARY

    p_line2 = doc.add_paragraph()
    p_line2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line2.paragraph_format.space_before = Pt(0)
    p_line2.paragraph_format.space_after = Pt(30)
    r_line2 = p_line2.add_run("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    r_line2.font.name = 'Times New Roman'
    r_line2.font.size = Pt(12)
    r_line2.font.color.rgb = COLOR_PRIMARY

    # Metadata Table
    meta_tbl = doc.add_table(rows=1, cols=2)
    meta_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_tbl.autofit = False
    meta_tbl.columns[0].width = Inches(3.25)
    meta_tbl.columns[1].width = Inches(3.25)
    
    c1 = meta_tbl.cell(0, 0)
    p_c1 = c1.paragraphs[0]
    p_c1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_c1.paragraph_format.line_spacing = 1.2
    r_c1_h = p_c1.add_run("SUBMITTED BY:\n")
    r_c1_h.font.name = 'Times New Roman'
    r_c1_h.font.size = Pt(11)
    r_c1_h.font.bold = True
    r_c1_h.font.color.rgb = COLOR_PRIMARY
    
    r_c1_b = p_c1.add_run("Name: [Student Name]\nRoll No: [Student Roll Number]\nSeat No: [Exam Seat Number]\nTYBCA Semester V")
    r_c1_b.font.name = 'Times New Roman'
    r_c1_b.font.size = Pt(10.5)
    r_c1_b.font.color.rgb = COLOR_TEXT

    c2 = meta_tbl.cell(0, 1)
    p_c2 = c2.paragraphs[0]
    p_c2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_c2.paragraph_format.line_spacing = 1.2
    r_c2_h = p_c2.add_run("UNDER THE GUIDANCE OF:\n")
    r_c2_h.font.name = 'Times New Roman'
    r_c2_h.font.size = Pt(11)
    r_c2_h.font.bold = True
    r_c2_h.font.color.rgb = COLOR_PRIMARY
    
    r_c2_b = p_c2.add_run("Prof. [Internal Guide Teacher Name]\nAssistant Professor / Project Guide\nDepartment of Computer Applications\nCollege Name / University")
    r_c2_b.font.name = 'Times New Roman'
    r_c2_b.font.size = Pt(10.5)
    r_c2_b.font.color.rgb = COLOR_TEXT

    # =============================================================
    # (ii) MINOR PROJECT COMPLETION CERTIFICATE
    # =============================================================
    doc.add_page_break()
    p_cert_head = doc.add_paragraph()
    p_cert_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_head.paragraph_format.space_before = Pt(12)
    p_cert_head.paragraph_format.space_after = Pt(4)
    r_ch = p_cert_head.add_run("DEPARTMENT OF COMPUTER APPLICATIONS\nCOLLEGE OF COMPUTER SCIENCE & INFORMATION TECHNOLOGY")
    r_ch.font.name = 'Times New Roman'
    r_ch.font.size = Pt(13)
    r_ch.font.bold = True
    r_ch.font.color.rgb = COLOR_PRIMARY
    
    p_cert_t = doc.add_paragraph()
    p_cert_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_t.paragraph_format.space_before = Pt(16)
    p_cert_t.paragraph_format.space_after = Pt(20)
    r_ct = p_cert_t.add_run("CERTIFICATE OF COMPLETION")
    r_ct.font.name = 'Times New Roman'
    r_ct.font.size = Pt(18)
    r_ct.font.bold = True
    r_ct.font.underline = True
    r_ct.font.color.rgb = COLOR_PRIMARY
    
    add_body_p(
        doc,
        "This is to certify that the Minor Project Report entitled \"GAMEKART — E-COMMERCE GAMING ACCESSORIES & HARDWARE STORE\" is a bona fide work carried out by the following student of Third Year Bachelor of Computer Applications (TYBCA), Semester V, during the Academic Year 2025–2026 in partial fulfillment of the requirements for the award of the Degree of Bachelor of Computer Applications (BCA) in Advanced Web Development (AWD) and Web Frameworks and Services (WFS)."
    )
    
    stud_table_data = [
        ["Sr. No.", "Candidate Full Name", "Roll Number", "University Seat No."],
        ["1.", "[Student Name]", "[Roll No]", "[Seat No]"]
    ]
    add_styled_table(doc, ["Sr. No.", "Candidate Full Name", "Roll Number", "University Seat No."], stud_table_data, col_widths=[0.8, 2.7, 1.5, 1.5], font_size=10.0)
    
    add_body_p(
        doc,
        "The project has been examined by the undersigned internal guide and examiners and is approved for submission in the semester examination."
    )
    
    p_dt = doc.add_paragraph()
    p_dt.paragraph_format.space_before = Pt(18)
    p_dt.paragraph_format.space_after = Pt(36)
    r_dt = p_dt.add_run("Date: _______________\nPlace: _______________")
    r_dt.font.name = 'Times New Roman'
    r_dt.font.size = Pt(11)
    r_dt.font.bold = True
    
    # Signature blocks
    sig_tbl = doc.add_table(rows=1, cols=3)
    sig_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    sig_tbl.autofit = False
    sig_tbl.columns[0].width = Inches(2.15)
    sig_tbl.columns[1].width = Inches(2.15)
    sig_tbl.columns[2].width = Inches(2.15)
    
    def format_sig_cell(cell, title, role):
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(f"\n\n_____________________\n{title}\n{role}")
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = COLOR_DARK
        
    format_sig_cell(sig_tbl.cell(0, 0), "Internal Guide", "Department of Computer Applications")
    format_sig_cell(sig_tbl.cell(0, 1), "Head of Department", "Department of Computer Applications")
    format_sig_cell(sig_tbl.cell(0, 2), "External Examiner", "University Examination Board")

    # =============================================================
    # (iii) INDEX / TABLE OF CONTENTS
    # =============================================================
    doc.add_page_break()
    add_heading_1(doc, "TABLE OF CONTENTS")
    
    index_data = [
        ["(i)", "Cover Page", "1"],
        ["(ii)", "Minor Project Completion Certificate", "2"],
        ["(iii)", "Table of Contents / Index", "3"],
        ["1.", "INTRODUCTION", "4"],
        ["", "1.1 Project Overview & Purpose", "4"],
        ["", "1.2 Problem Statement & Motivation", "4"],
        ["", "1.3 Scope of the Project", "5"],
        ["", "1.4 Target Audience & User Profiles", "5"],
        ["", "1.5 System Features & Key Highlights", "6"],
        ["2.", "TECHNOLOGY USED", "7"],
        ["", "2.1 AWD & WFS Full-Stack Architecture", "7"],
        ["", "2.2 Frontend Framework & Tooling (React 18 & Vite)", "7"],
        ["", "2.3 Backend & Web Services (Node.js & Express.js)", "8"],
        ["", "2.4 Database & Object Modeling (MongoDB & Mongoose)", "9"],
        ["", "2.5 Hardware & Software Requirements", "10"],
        ["3.", "OBJECTIVES", "11"],
        ["", "3.1 Primary Goals & Vision", "11"],
        ["", "3.2 Technical Objectives (AWD & WFS Competencies)", "11"],
        ["", "3.3 Functional Objectives for End-Users", "12"],
        ["", "3.4 Functional Objectives for Administrators", "12"],
        ["", "3.5 Non-Functional Quality Objectives", "13"],
        ["4.", "SYSTEM FLOW CHART & ARCHITECTURE", "14"],
        ["", "4.1 Full-Stack System Architecture Diagram", "14"],
        ["", "4.2 Customer Registration & Browsing Flow Chart", "15"],
        ["", "4.3 Shopping Cart & Order Placement Flow Chart", "16"],
        ["", "4.4 Administrator Inventory & Order Management Flow Chart", "17"],
        ["", "4.5 Data Flow Diagrams (DFD Level 0 & DFD Level 1)", "18"],
        ["5.", "DATABASE DESIGN & API CONTRACTS", "19"],
        ["", "5.1 Database Overview & Architecture (dbProject)", "19"],
        ["", "5.2 Entity Relationship (ER) Conceptual Model", "19"],
        ["", "5.3 Detailed Data Dictionaries (products, registers, admins, carts)", "20"],
        ["", "5.4 RESTful Web API Specifications & Endpoints Data Contract", "22"],
        ["6.", "SYSTEM IMPLEMENTATION & QUALITY ASSURANCE", "23"],
        ["", "6.1 Core Functional Modules Breakdown", "23"],
        ["", "6.2 Software Testing & Comprehensive Test Cases (TC-01 to TC-13)", "24"],
        ["7.", "SCREEN SHOTS & USER INTERFACE SHOWCASE", "25"],
        ["", "7.1 Customer Shopping Store UI Screenshots (Figures 1 to 7)", "25"],
        ["", "7.2 Admin Management Portal UI Screenshots (Figures 8 to 10)", "27"],
        ["", "7.3 High-Resolution Hardware & Gaming Product Showcase (Figures 11 to 16)", "28"],
        ["8.", "CONCLUSION & FUTURE ENHANCEMENTS", "29"],
        ["", "8.1 Project Conclusion & Academic Summary", "29"],
        ["", "8.2 Future Enhancements & Roadmap", "29"],
        ["9.", "REFERENCES & BIBLIOGRAPHY", "30"],
        ["", "9.1 Academic Textbooks & Publications", "30"],
        ["", "9.2 Official Web Documentation & Online Resources", "30"]
    ]
    add_styled_table(doc, ["No.", "Topic / Chapter Name", "Page No."], index_data, col_widths=[0.8, 4.8, 0.9], font_size=9.5)

    # =============================================================
    # (iv) CHAPTER 1: INTRODUCTION
    # =============================================================
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 1: INTRODUCTION")
    
    add_heading_2(doc, "1.1 Project Overview & Purpose")
    add_body_p(
        doc,
        "In the modern digital era, the global gaming industry has expanded exponentially, commanding a multi-billion dollar economy. Enthusiasts, competitive e-sports athletes, and casual gamers require specialized hardware, including next-generation gaming consoles, mechanical RGB keyboards, ultra-high refresh rate curved displays, ergonomic gaming chairs, spatial audio headsets, and high-precision wireless mice."
    )
    add_body_p(
        doc,
        "GAMEKART is a comprehensive, production-ready Full-Stack E-Commerce Web Application specifically engineered for retail gaming gear and hardware accessories. Built as an academic minor project for TYBCA Semester V under the courses Advanced Web Development (AWD) and Web Frameworks and Services (WFS), GameKart demonstrates modern architectural patterns including dual-port micro-services, reactive client-side rendering, RESTful Web API design, multipart file uploads, and scalable document-oriented database modeling."
    )
    
    add_callout(
        doc,
        "GameKart bridges the gap between high-performance reactive user interfaces and robust server-side APIs, utilizing React 18, Node.js, Express.js, and MongoDB Community Server.",
        "Key Project Distinction"
    )

    add_heading_2(doc, "1.2 Problem Statement & Current Challenges")
    add_body_p(
        doc,
        "Traditional brick-and-mortar retail gaming shops and legacy multi-vendor e-commerce websites suffer from significant bottlenecks:"
    )
    add_bullet_p(doc, "Fragmented product information with poor visual representation of gaming specifications.", bold_prefix="1. Lack of Niche Specialization: ")
    add_bullet_p(doc, "Slow page loads caused by server-side monolithic rendering cycles and bloated asset pipelines.", bold_prefix="2. High Latency & Slow Rendering: ")
    add_bullet_p(doc, "Absence of real-time client-side search and instant catalog filtering.", bold_prefix="3. Poor Search & Discovery: ")
    add_bullet_p(doc, "Complex, clunky administrative dashboards requiring specialized training for simple inventory updates.", bold_prefix="4. Inefficient Inventory Tools: ")
    add_bullet_p(doc, "Lack of isolated backend micro-services, creating security vulnerabilities between customer traffic and admin operations.", bold_prefix="5. Monolithic Architecture Risks: ")

    add_heading_2(doc, "1.3 Scope of the Project")
    add_body_p(
        doc,
        "The GameKart platform encompasses end-to-end e-commerce operations split across two distinct portals:"
    )
    add_bullet_p(doc, "Interactive storefront allowing customers to discover products, filter by keywords, inspect hardware specifications, create personal accounts with avatars, add items to a persistent shopping cart, and track order fulfillment history.", bold_prefix="A. Customer Client Portal (Port 5174 / API Port 4000): ")
    add_bullet_p(doc, "Secure administrative dashboard enabling store operators to upload hardware products with images via multipart forms, edit prices and descriptions, inspect aggregated customer orders with joined database lookups, and audit registered user accounts.", bold_prefix="B. Admin Control Center (Port 5173 / API Port 5000): ")

    add_heading_2(doc, "1.4 Target Audience & User Profiles")
    add_body_p(
        doc,
        "GameKart caters to three primary stakeholder personas:"
    )
    user_personas = [
        ["Persona", "Role", "Key Needs & Behaviors", "Platform Touchpoints"],
        ["Gamers & Hardware Enthusiasts", "End-User / Customer", "Fast searching, rich visual previews, clear pricing, instant cart addition, simple checkout.", "Client UI (Port 5174), Catalog, Cart, Order History"],
        ["Store Administrator", "Manager / Operator", "Rapid product publishing with photo uploads, price updates, order review, customer directory auditing.", "Admin UI (Port 5173), Inventory Manager, Order Center"],
        ["Academic Evaluator", "Faculty / Examiner", "Review of clean code structure, RESTful API conventions, database normalization/schemas, and system documentation.", "Full Documentation, Source Code, Database Architecture"]
    ]
    add_styled_table(doc, ["Persona", "Role", "Key Needs & Behaviors", "Platform Touchpoints"], user_personas, col_widths=[1.5, 1.2, 2.3, 1.5], font_size=9.0)

    add_heading_2(doc, "1.5 System Features & Key Highlights")
    add_bullet_p(doc, "Sub-second client-side filtering without redundant network requests.", bold_prefix="Instant Search & Filter: ")
    add_bullet_p(doc, "Multer disk storage pipeline with automated lowercase normalization and static hosting.", bold_prefix="Multipart Image Uploads: ")
    add_bullet_p(doc, "Isolated ports for Client Frontend (5174), Admin Frontend (5173), Client API (4000), and Admin API (5000).", bold_prefix="Dual-Port Architecture: ")
    add_bullet_p(doc, "MongoDB Aggregation Pipeline ($lookup) to combine carts, users, and products seamlessly.", bold_prefix="Relational Aggregations: ")

    # =============================================================
    # (v) CHAPTER 2: TECHNOLOGY USED
    # =============================================================
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 2: TECHNOLOGY USED")
    
    add_heading_2(doc, "2.1 AWD & WFS Full-Stack Architecture")
    add_body_p(
        doc,
        "The GameKart application is constructed using the modern MERN technology stack (MongoDB, Express.js, React, Node.js), incorporating Advanced Web Development (AWD) principles and Web Frameworks and Services (WFS) concepts. The architecture decouples the presentation layer from backend business logic and database persistence."
    )
    
    tech_overview = [
        ["Layer", "Technology", "Version", "Role & Description"],
        ["Frontend UI", "React.js", "18.3.x", "Component-based reactive user interface rendering"],
        ["Frontend Build Tool", "Vite", "5.4.x", "Lightning-fast HMR (Hot Module Replacement) bundler"],
        ["Frontend Styling", "Vanilla CSS3", "CSS3 Standard", "Glassmorphic cards, responsive flex/grid, modern dark themes"],
        ["Backend Runtime", "Node.js", "20.x LTS", "Non-blocking, event-driven JavaScript server environment"],
        ["Web Framework", "Express.js", "4.19.x", "RESTful routing, middleware handling, static asset serving"],
        ["File Uploads", "Multer", "1.4.x", "Multipart/form-data processing and disk storage management"],
        ["Database Server", "MongoDB Community", "8.0.x", "High-performance NoSQL document-oriented database"],
        ["Object Modeling", "Mongoose", "8.x", "Schema validation, type casting, and query middleware"],
        ["Cross-Origin Security", "CORS Middleware", "2.8.x", "Origin resource sharing policy enforcement"]
    ]
    add_styled_table(doc, ["Layer", "Technology", "Version", "Role & Description"], tech_overview, col_widths=[1.2, 1.4, 0.9, 3.0], font_size=9.0)

    add_heading_2(doc, "2.2 Frontend Framework & Tooling")
    add_body_p(
        doc,
        "The client application is built with React 18, leveraging the Virtual DOM for ultra-efficient UI reconciliation. Vite provides development speed with ES modules and instant page reloads."
    )
    add_bullet_p(doc, "Enables reusable components such as ProductCard, Navbar, Footer, and OrderRow.", bold_prefix="React Component Model: ")
    add_bullet_p(doc, "Manages client-side state dynamically using `useState`, `useEffect`, and `useNavigate` hooks.", bold_prefix="React Hooks: ")
    add_bullet_p(doc, "Provides multi-page navigation without browser refresh cycles.", bold_prefix="React Router DOM: ")

    add_heading_2(doc, "2.3 Backend & Web Services (WFS)")
    add_body_p(
        doc,
        "The backend services are structured as two lightweight Express.js micro-servers:"
    )
    add_bullet_p(doc, "Handles customer registration, authentication, product catalog delivery, cart additions, and order creation.", bold_prefix="1. Client Web Service (Port 4000): ")
    add_bullet_p(doc, "Handles administrative product creation, image uploading via Multer, product deletion, user auditing, and aggregate order queries.", bold_prefix="2. Admin Web Service (Port 5000): ")

    add_heading_2(doc, "2.4 Database & Object Modeling")
    add_body_p(
        doc,
        "MongoDB stores data as flexible BSON documents. Mongoose schemas enforce data integrity, defining strict types and required fields for all entities in `dbProject`."
    )

    add_heading_2(doc, "2.5 Hardware & Software Requirements")
    hw_sw_data = [
        ["Component", "Minimum Requirement", "Recommended Specification"],
        ["Processor (CPU)", "Dual-Core Intel / AMD 2.0 GHz", "Quad-Core Intel Core i5 / AMD Ryzen 5 or higher"],
        ["System Memory (RAM)", "4 GB DDR3 / DDR4", "8 GB / 16 GB DDR4 or DDR5 RAM"],
        ["Hard Disk Space", "2 GB free storage", "10 GB SSD storage for assets & database"],
        ["Operating System", "Windows 10 / 11, Linux (Ubuntu), macOS", "Windows 11 (64-bit) / macOS Sonoma"],
        ["Runtime Environment", "Node.js v18.x with npm v9.x", "Node.js v20.x LTS with npm v10.x"],
        ["Database Engine", "MongoDB Community Server 7.x", "MongoDB Community Server 8.0 with Compass"],
        ["Web Browser", "Edge 100+, Chrome 100+, Firefox 90+", "Latest Microsoft Edge or Google Chrome"]
    ]
    add_styled_table(doc, ["Component", "Minimum Requirement", "Recommended Specification"], hw_sw_data, col_widths=[1.5, 2.5, 2.5], font_size=9.0)

    # =============================================================
    # (vi) CHAPTER 3: OBJECTIVES
    # =============================================================
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 3: OBJECTIVES")
    
    add_heading_2(doc, "3.1 Primary Goals & Vision")
    add_body_p(
        doc,
        "The overarching vision of the GameKart project is to construct a scalable, resilient, and aesthetically captivating e-commerce platform tailored specifically for gaming gear, demonstrating the practical application of Advanced Web Development and Web Services methodologies taught in the BCA curriculum."
    )

    add_heading_2(doc, "3.2 Academic & Technical Objectives")
    add_bullet_p(doc, "Master the full development lifecycle of a modern Single Page Application (SPA) using React 18 and Vite.", bold_prefix="1. SPA Architecture: ")
    add_bullet_p(doc, "Design RESTful APIs following standard HTTP verbs (GET, POST, PUT, DELETE) and JSON payloads.", bold_prefix="2. RESTful Web Services: ")
    add_bullet_p(doc, "Gain hands-on expertise in NoSQL schema design, Mongoose models, and cross-collection lookups.", bold_prefix="3. Database Modeling: ")
    add_bullet_p(doc, "Implement secure multipart/form-data upload handling with file validation and static directory exposure.", bold_prefix="4. File Handling: ")
    add_bullet_p(doc, "Maintain modular, readable, and clean code separating client UI, admin controls, and API layers.", bold_prefix="5. Code Maintainability: ")

    add_heading_2(doc, "3.3 Functional Objectives for End-Users")
    add_bullet_p(doc, "Allow users to view rich gaming catalogs with prices, high-res photos, and detailed descriptions.", bold_prefix="Catalogue Exploration: ")
    add_bullet_p(doc, "Provide instant real-time search filtering on title and category without reloading.", bold_prefix="Real-Time Search: ")
    add_bullet_p(doc, "Enable secure account registration with custom avatar photo upload and credential validation.", bold_prefix="User Account Management: ")
    add_bullet_p(doc, "Facilitate one-click addition of products to an active cart and instant order confirmation.", bold_prefix="Cart & Checkout: ")
    add_bullet_p(doc, "Allow customers to review all previous purchases with date stamps and product thumbnails.", bold_prefix="Order Tracking: ")

    add_heading_2(doc, "3.4 Functional Objectives for Administrators")
    add_bullet_p(doc, "Provide a streamlined form to create new gaming products with multipart image upload.", bold_prefix="Product Insertion: ")
    add_bullet_p(doc, "Allow instant deletion and inventory updates for out-of-stock or obsolete hardware.", bold_prefix="Catalog Management: ")
    add_bullet_p(doc, "Display an aggregated view of all placed orders with customer details and item pictures.", bold_prefix="Order Inspection: ")
    add_bullet_p(doc, "Provide a clean table auditing all registered users with emails, cities, and profile images.", bold_prefix="User Directory: ")

    add_heading_2(doc, "3.5 Non-Functional Quality Objectives")
    nfr_data = [
        ["Attribute", "Specification & Goal", "Implementation Technique"],
        ["Performance", "Page load times under 1.5 seconds; search latency under 50ms", "Vite bundling, client-side filtering, lightweight REST JSON"],
        ["Security", "Protection against unauthorized mutations; origin restriction", "CORS middleware, port isolation (5000 vs 4000), input sanitization"],
        ["Reliability", "Zero data loss during orders; robust database transactions", "Mongoose schema constraints, error handling middleware"],
        ["Usability", "Responsive layout across desktop, tablet, and mobile displays", "CSS Flexbox, CSS Grid, media queries, high-contrast gaming theme"],
        ["Maintainability", "Modular code architecture with clear component boundaries", "Separation of client and admin directories, reusable React components"]
    ]
    add_styled_table(doc, ["Attribute", "Specification & Goal", "Implementation Technique"], nfr_data, col_widths=[1.2, 2.5, 2.8], font_size=9.0)

    # =============================================================
    # (vii) CHAPTER 4: SYSTEM FLOW CHART & ARCHITECTURE
    # =============================================================
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 4: SYSTEM FLOW CHART & ARCHITECTURE")
    
    add_heading_2(doc, "4.1 Full-Stack System Architecture")
    add_body_p(
        doc,
        "GameKart follows a decoupled, 3-Tier Multi-Port Micro-Architecture. The presentation layer (React Portals) communicates via asynchronous HTTP AJAX calls with the Express.js Web Services layer, which in turn interacts with the MongoDB persistence engine."
    )
    
    arch_code = """
+-----------------------------------------------------------------------------------+
|                            PRESENTATION TIER (FRONTEND)                          |
|                                                                                   |
|   +------------------------------------+   +------------------------------------+ |
|   |  Customer Storefront (React/Vite) |   |    Admin Portal (React/Vite)       | |
|   |        http://localhost:5174       |   |        http://localhost:5173       | |
|   |  (Home, Products, Cart, Orders)   |   |   (Products, Orders, Users Tables) | |
|   +-----------------+------------------+   +-----------------+------------------+ |
+---------------------|----------------------------------------|--------------------+
                      | HTTP JSON / Multipart                  | HTTP JSON / Multipart
                      v                                        v
+-----------------------------------------------------------------------------------+
|                           APPLICATION & WEB SERVICES TIER                         |
|                                                                                   |
|   +------------------------------------+   +------------------------------------+ |
|   |    Client API Server (Node/Express)|   |    Admin API Server (Node/Express) | |
|   |        http://localhost:4000       |   |        http://localhost:5000       | |
|   |  (Auth, Product Fetch, Cart Sync)  |   |   (Multer Uploads, Inventory CRUD) | |
|   +-----------------+------------------+   +-----------------+------------------+ |
|                     | Static File Serving: /uploads/         |                    |
+---------------------|----------------------------------------|--------------------+
                      | Mongoose ODM Query Engine              | Mongoose ODM
                      v                                        v
+-----------------------------------------------------------------------------------+
|                             DATABASE PERSISTENCE TIER                             |
|                                                                                   |
|                        MongoDB Community Server 8.0.x                             |
|                             mongodb://localhost:27017                             |
|                                                                                   |
|   [dbProject.products]   [dbProject.registers]   [dbProject.carts]   [admins]     |
+-----------------------------------------------------------------------------------+
"""
    add_code_block(doc, arch_code, "Figure 4.1 – GameKart 3-Tier Multi-Port System Architecture")

    add_heading_2(doc, "4.2 Customer Registration & Browsing Flow Chart")
    add_body_p(
        doc,
        "The customer interaction workflow guides users from account onboarding to browsing the interactive catalog:"
    )
    user_flow = """
[Start] ──> [Open http://localhost:5174/] ──> [Browse Home Showcase]
                  │
                  ├──> [Already Registered?] ──Yes──> [Enter Email & Password] ──> [Login Success (Store ID)]
                  │                                                                       │
                  └──No──> [Fill Signup Form + Upload Avatar] ──> [POST /signup] ─────────┘
                                                                       │
                                                                       v
[View Product Catalog] <───────────────────────────────────────────────┘
         │
         ├──> [Type Keyword in Search Bar] ──> [Instant Filtered Product Grid]
         │
         └──> [Click 'Get More Info'] ──> [Open Product Details Modal / Specs]
                                                    │
                                                    v
                                        [Click 'Add to Cart']
                                                    │
                                                    v
                                          [POST /addToCart]
"""
    add_code_block(doc, user_flow, "Figure 4.2 – Customer Onboarding & Catalog Discovery Workflow")

    doc.add_page_break()
    add_heading_2(doc, "4.3 Shopping Cart & Order Placement Flow Chart")
    add_body_p(
        doc,
        "The order processing pipeline coordinates between the customer's cart, database insertion, and order history records:"
    )
    order_flow = """
[Product in Cart] ──> [Open /orders Route] ──> [GET /getCart / User ID]
                             │
                             ├──> [Review Items, Quantities & Unit Prices]
                             │
                             ├──> [Option: Remove Item] ──> [DELETE /delCart/:id] ──> [Cart Refreshed]
                             │
                             └──> [Click 'Order Now']
                                         │
                                         v
                                  [PUT /orderNow]
                                         │
                                         v
                            [Database Update: status='ordered']
                                         │
                                         v
                         [Display Success Toast / Confirmation]
                                         │
                                         v
                        [Item Visible in Admin Order Dashboard]
"""
    add_code_block(doc, order_flow, "Figure 4.3 – Shopping Cart Checkout & Order Placement Workflow")

    add_heading_2(doc, "4.4 Administrator Inventory & Order Management Flow Chart")
    admin_flow = """
[Start Admin] ──> [Open http://localhost:5173/] ──> [Enter Admin Credentials]
                         │
                         v
            [Admin Dashboard Navigation]
             │                     │
             ├──> [Product Hub]    ├──> [Orders Hub (/orders)]    ├──> [Users Hub (/users)]
             │         │                     │                              │
             │   [Fill Form]                 v                              v
             │   [Upload Photo]     [GET /orders with $lookup]    [GET /users on Port 5000]
             │   [POST /products]            │                              │
             │         │                     v                              v
             │   [New Item Live]    [Inspect Buyer & Price]       [Review Customer Table]
             │         │
             │   [Delete Item]
             │   [DELETE /Delproducts/:id]
"""
    add_code_block(doc, admin_flow, "Figure 4.4 – Administrator Inventory & Order Workflow")

    add_heading_2(doc, "4.5 Data Flow Diagrams (DFD Level 0 & Level 1)")
    add_body_p(
        doc,
        "Data Flow Diagrams depict how information traverses between external entities, application processes, and data stores."
    )
    dfd_0 = """
                      +---------------------------------------+
                      |               CUSTOMER                |
                      +---------------------------------------+
                        |  ^                      ^         |
       Registration Data|  |Auth Token / Products |Order Req|Order History
                        v  |                      |         v
                  +-----------------------------------------------+
                  |                   PROCESS 0:                  |
                  |          GAMEKART E-COMMERCE SYSTEM           |
                  +-----------------------------------------------+
                        ^  |                      ^         |
        Admin Auth /    |  |Inventory Updates /   |Order    |Customer Records
        Product Uploads |  |Aggregated Order Data |Lookup   v
                        v  |                      |
                      +---------------------------------------+
                      |             ADMINISTRATOR             |
                      +---------------------------------------+
"""
    add_code_block(doc, dfd_0, "Figure 4.5 – DFD Level 0 (Context Diagram)")

    # =============================================================
    # (viii) CHAPTER 5: DATABASE DESIGN
    # =============================================================
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 5: DATABASE DESIGN & API CONTRACTS")
    
    add_heading_2(doc, "5.1 Database Overview & Architecture")
    add_body_p(
        doc,
        "GameKart utilizes MongoDB Community Server 8.x under the database name `dbProject`. The schema is managed through Mongoose ODM, enforcing strict data typing, default values, and relational consistency across four collections."
    )

    add_heading_2(doc, "5.2 Entity Relationship (ER) Conceptual Model")
    add_body_p(
        doc,
        "Although MongoDB is a document-oriented database, GameKart maintains structured relational dependencies through ObjectIds:"
    )
    add_bullet_p(doc, "One customer (`registers`) can create multiple orders and cart entries (`carts`) [1 : N Relationship].", bold_prefix="1. User to Cart/Order: ")
    add_bullet_p(doc, "One catalog product (`products`) can be referenced across multiple customer carts (`carts`) [1 : N Relationship].", bold_prefix="2. Product to Cart: ")
    add_bullet_p(doc, "Administrators manage the central catalog of products and review all user orders [1 : N Management].", bold_prefix="3. Admin to Products: ")

    add_heading_2(doc, "5.3 Detailed Data Dictionaries")
    
    add_heading_3(doc, "5.3.1 Collection: 'products' (Gaming Gear Catalog)")
    prod_fields = [
        ["Field Name", "Data Type", "Constraints", "Default", "Description & Purpose"],
        ["_id", "ObjectId", "Primary Key, Auto-gen", "Auto", "Unique MongoDB document identifier"],
        ["pname", "String", "Required, Trimmed", "None", "Name of gaming accessory / console"],
        ["pimg", "String", "Required", "None", "Filename of uploaded image in /uploads/"],
        ["description", "String", "Required", "None", "Hardware specifications and features"],
        ["price", "Number / String", "Required, > 0", "None", "Retail price in Indian Rupees (INR)"],
        ["createdAt", "Date", "System Timestamp", "Date.now()", "Timestamp of product publication"]
    ]
    add_styled_table(doc, ["Field Name", "Data Type", "Constraints", "Default", "Description & Purpose"], prod_fields, col_widths=[1.1, 1.0, 1.3, 1.0, 2.1], font_size=8.5)

    add_heading_3(doc, "5.3.2 Collection: 'registers' (Customer Accounts)")
    reg_fields = [
        ["Field Name", "Data Type", "Constraints", "Default", "Description & Purpose"],
        ["_id", "ObjectId", "Primary Key, Auto-gen", "Auto", "Unique customer account ID"],
        ["name", "String", "Required, Max: 100", "None", "Full name of customer"],
        ["email", "String", "Required, Unique, Lowercase", "None", "User login email address"],
        ["password", "String", "Required, Min: 3", "None", "Account password (hashed or plain)"],
        ["gender", "String", "Enum: Male/Female/Other", "Male", "Gender identification"],
        ["city", "String", "Required", "None", "Delivery and residential city"],
        ["profile", "String", "Optional", "default.png", "Avatar image filename in /uploads/"]
    ]
    add_styled_table(doc, ["Field Name", "Data Type", "Constraints", "Default", "Description & Purpose"], reg_fields, col_widths=[1.1, 1.0, 1.3, 1.0, 2.1], font_size=8.5)

    doc.add_page_break()
    add_heading_3(doc, "5.3.3 Collection: 'admins' (Store Management Credentials)")
    adm_fields = [
        ["Field Name", "Data Type", "Constraints", "Default", "Description & Purpose"],
        ["_id", "ObjectId", "Primary Key, Auto-gen", "Auto", "Unique admin identifier"],
        ["name", "String", "Required", "Admin", "Administrative username"],
        ["email", "String", "Required, Unique", "admin@gamekart.com", "Admin authentication email"],
        ["password", "String", "Required", "admin", "Admin security credential"]
    ]
    add_styled_table(doc, ["Field Name", "Data Type", "Constraints", "Default", "Description & Purpose"], adm_fields, col_widths=[1.1, 1.0, 1.3, 1.0, 2.1], font_size=8.5)

    add_heading_3(doc, "5.3.4 Collection: 'carts' (Shopping Cart & Order History)")
    cart_fields = [
        ["Field Name", "Data Type", "Constraints", "Default", "Description & Purpose"],
        ["_id", "ObjectId", "Primary Key, Auto-gen", "Auto", "Unique cart record ID"],
        ["user_id", "ObjectId / String", "Required, FK -> registers", "None", "ID of the customer who added item"],
        ["product_id", "ObjectId / String", "Required, FK -> products", "None", "ID of the referenced product"],
        ["pname", "String", "Required", "None", "Cached product title for fast lookups"],
        ["price", "Number / String", "Required", "None", "Unit price at time of cart addition"],
        ["pimg", "String", "Required", "None", "Cached product image filename"],
        ["status", "String", "Enum: 'cart' | 'ordered'", "'cart'", "Current transaction lifecycle status"],
        ["order_date", "Date", "System Timestamp", "Date.now()", "Date of order placement"]
    ]
    add_styled_table(doc, ["Field Name", "Data Type", "Constraints", "Default", "Description & Purpose"], cart_fields, col_widths=[1.1, 1.0, 1.3, 1.0, 2.1], font_size=8.5)

    add_heading_2(doc, "5.4 RESTful Web API Specifications & Endpoints Data Contract")
    api_endpoints = [
        ["Port", "Method", "Endpoint URI", "Request Payload", "Response Status", "Purpose"],
        ["4000", "GET", "/getProducts", "None", "200 OK (JSON Array)", "Fetch active product catalog"],
        ["4000", "POST", "/signup", "Multipart (name, email, pass, file)", "201 Created", "Register new customer"],
        ["4000", "POST", "/login", "JSON {email, password}", "200 OK / 401 Unauthorized", "Authenticate customer"],
        ["4000", "POST", "/addToCart", "JSON {userId, prodId, pname, price}", "200 OK", "Insert item into cart"],
        ["4000", "GET", "/getCart", "Query param / header", "200 OK (Cart Array)", "Fetch customer cart items"],
        ["4000", "GET", "/getProduct/:id", "URL Param :id", "200 OK (Single Product)", "Fetch details of one item"],
        ["5000", "POST", "/products", "Multipart (pname, price, desc, pimg)", "201 Created", "Admin upload new product"],
        ["5000", "PUT", "/updateProducts/:id", "JSON {pname, price, desc}", "200 OK", "Admin update product info"],
        ["5000", "DELETE", "/Delproducts/:id", "URL Param :id", "200 OK", "Admin remove product"],
        ["5000", "GET", "/orders", "None", "200 OK (Aggregated List)", "Admin fetch joined orders"],
        ["5000", "GET", "/users", "None", "200 OK (User Array)", "Admin fetch user directory"]
    ]
    add_styled_table(doc, ["Port", "Method", "Endpoint URI", "Request Payload", "Response Status", "Purpose"], api_endpoints, col_widths=[0.6, 0.7, 1.5, 1.5, 1.1, 1.1], font_size=8.0)

    # =============================================================
    # (ix) CHAPTER 6: SYSTEM IMPLEMENTATION & QA
    # =============================================================
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 6: SYSTEM IMPLEMENTATION & QUALITY ASSURANCE")
    
    add_heading_2(doc, "6.1 Core Functional Modules Breakdown")
    add_bullet_p(doc, "Built using React Controlled Form components with multipart file input for profile picture uploads. Authenticates against MongoDB with session persistence.", bold_prefix="Module 1 – Customer Authentication (Client): ")
    add_bullet_p(doc, "Fetches JSON catalog from `http://localhost:4000/getProducts` and binds state to dynamic search filters with sub-second reactivity.", bold_prefix="Module 2 – Interactive Product Catalog (Client): ")
    add_bullet_p(doc, "Manages cart array, calculating total price dynamically and updating transaction status from 'cart' to 'ordered' upon checkout.", bold_prefix="Module 3 – Shopping Cart & Checkout Engine (Client): ")
    add_bullet_p(doc, "Express route utilizing Multer `diskStorage` engine to validate, sanitize, and save product pictures to `/uploads/` while inserting BSON documents into MongoDB.", bold_prefix="Module 4 – Admin Inventory & Upload Service (Admin): ")
    add_bullet_p(doc, "Combines `carts`, `registers`, and `products` records using MongoDB `$lookup` aggregations to display comprehensive order details.", bold_prefix="Module 5 – Admin Order Auditing Service (Admin): ")

    add_heading_2(doc, "6.2 Software Testing & Comprehensive Test Cases (TC-01 to TC-13)")
    add_body_p(
        doc,
        "The system underwent rigorous black-box functional testing, REST API validation, and boundary value analysis:"
    )
    gk_tests = [
        ["Test ID", "Module", "Scenario", "Input / Precondition", "Expected Result", "Status"],
        ["TC-01", "Client Auth", "User Registration", "Valid name, email, password, avatar", "201 Created; record in MongoDB", "Pass"],
        ["TC-02", "Client Auth", "User Login", "Registered email & password", "200 OK; login success; ID saved", "Pass"],
        ["TC-03", "Client Auth", "Invalid Login", "Unregistered email / wrong password", "401 Unauthorized; alert shown", "Pass"],
        ["TC-04", "Products", "Fetch Products", "GET /getProducts endpoint", "200 OK; array of items returned", "Pass"],
        ["TC-05", "Products", "Live Search", "Type 'Controller' in search bar", "Product grid dynamically filters", "Pass"],
        ["TC-06", "Cart", "Add to Cart", "Click 'Add to Cart' button", "200 OK; item inserted into carts", "Pass"],
        ["TC-07", "Cart", "Order Placement", "Click 'Order Now' in cart", "200 OK; status becomes 'ordered'", "Pass"],
        ["TC-08", "Admin Auth", "Admin Login", "admin@gamekart.com / admin", "200 OK; redirects to dashboard", "Pass"],
        ["TC-09", "Admin Prod", "Add Product", "Multipart name, price, photo", "201 Created; image saved to /uploads", "Pass"],
        ["TC-10", "Admin Prod", "Update Product", "PUT /updateProducts/:id", "200 OK; updated in MongoDB", "Pass"],
        ["TC-11", "Admin Prod", "Delete Product", "DELETE /Delproducts/:id", "200 OK; item removed from DB", "Pass"],
        ["TC-12", "Admin Order", "View Orders", "GET /orders with $lookup", "200 OK; returns joined order rows", "Pass"],
        ["TC-13", "Admin Users", "User Directory", "GET /users on Port 5000", "200 OK; displays all user records", "Pass"]
    ]
    add_styled_table(doc, ["ID", "Module", "Scenario", "Input", "Expected Result", "Status"], gk_tests, col_widths=[0.6, 0.9, 1.2, 1.6, 1.6, 0.6], font_size=8.0)

    # =============================================================
    # (ix) CHAPTER 7: SCREEN SHOTS & USER INTERFACE SHOWCASE
    # =============================================================
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 7: SCREEN SHOTS & USER INTERFACE SHOWCASE")
    
    add_heading_2(doc, "7.1 Customer Shopping Store UI Screenshots (Port 5174)")
    add_body_p(
        doc,
        "The following screenshots depict the live customer interface captured directly from the running Vite development server at http://localhost:5174/."
    )
    
    client_shots = [
        ("screenshots/client_home.png", "Figure 7.1 – GameKart Customer Storefront Homepage & Hero Banner"),
        ("screenshots/client_products.png", "Figure 7.2 – Interactive Gaming Products Catalog with Real-Time Search Bar"),
        ("screenshots/client_product_detail.png", "Figure 7.3 – Detailed Product Specifications & Add-to-Cart Interface"),
        ("screenshots/client_signup.png", "Figure 7.4 – Customer Account Registration & Profile Photo Upload Form"),
        ("screenshots/client_login.png", "Figure 7.5 – Customer Authentication & Secure Login Portal"),
        ("screenshots/client_orders.png", "Figure 7.6 – Customer Shopping Cart & Order Tracking Overview"),
        ("screenshots/client_contact.png", "Figure 7.7 – Customer Support, Inquiries & Contact Us Interface")
    ]
    for img_p, cap in client_shots:
        if os.path.exists(img_p):
            add_figure_image(doc, img_p, cap, width_in=5.4, space_after=4)
            doc.add_page_break()

    add_heading_2(doc, "7.2 Admin Management Portal UI Screenshots (Port 5173)")
    add_body_p(
        doc,
        "The following screenshots showcase the administrative management portal running at http://localhost:5173/."
    )
    
    admin_shots = [
        ("screenshots/admin_manage_products.png", "Figure 7.8 – Admin Product Catalog Management & Upload Dashboard"),
        ("screenshots/admin_orders.png", "Figure 7.9 – Admin Customer Orders Review & Fulfillment Dashboard"),
        ("screenshots/admin_users.png", "Figure 7.10 – Admin Registered User Accounts & Customer Directory")
    ]
    for img_p, cap in admin_shots:
        if os.path.exists(img_p):
            add_figure_image(doc, img_p, cap, width_in=5.4, space_after=4)
            doc.add_page_break()

    add_heading_2(doc, "7.3 High-Resolution Hardware & Gaming Product Showcase")
    add_body_p(
        doc,
        "Below are high-resolution product photography assets stored in `/uploads/` and dynamically rendered in the GameKart catalog:"
    )
    
    prod_shots = [
        ("client/src/uploads/console-ps5.jpg", "Figure 7.11 – Sony PlayStation 5 Next-Gen Gaming Console (Ultra HD 4K)"),
        ("client/src/uploads/controller-rgb.jpg", "Figure 7.12 – Wireless RGB DualSense Pro Gaming Controller"),
        ("client/src/uploads/curved-monitor.jpg", "Figure 7.13 – 34-Inch Ultra-Wide 165Hz Curved Gaming Monitor"),
        ("client/src/uploads/gaming-chair.jpg", "Figure 7.14 – Ergonomic Lumbar Support Racing Pro Gaming Chair"),
        ("client/src/uploads/headphone-pro.jpg", "Figure 7.15 – 7.1 Spatial Audio Wireless Noise-Cancelling Headset"),
        ("client/src/uploads/keyboard-mechanical.jpg", "Figure 7.16 – RGB Mechanical Gaming Keyboard with Custom Blue Switches")
    ]
    for img_p, cap in prod_shots:
        if os.path.exists(img_p):
            add_figure_image(doc, img_p, cap, width_in=4.2, space_after=4)

    # =============================================================
    # (x) CHAPTER 8: CONCLUSION & REFERENCES
    # =============================================================
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 8: CONCLUSION & FUTURE ENHANCEMENTS")
    
    add_heading_2(doc, "8.1 Project Conclusion & Academic Summary")
    add_body_p(
        doc,
        "The GAMEKART E-Commerce Gaming Accessories & Hardware Store has been successfully designed, developed, and evaluated in accordance with the TYBCA Semester V curriculum for Advanced Web Development (AWD) and Web Frameworks and Services (WFS). The project effectively implements a full-stack MERN architecture featuring dual-port isolation, reactive client-side rendering with React 18 and Vite, RESTful Web API endpoints with Express.js, multipart image uploads via Multer, and document database storage with MongoDB Community Server."
    )
    add_body_p(
        doc,
        "The system satisfies all functional requirements including user authentication, real-time product filtering, cart lifecycle management, multipart product publishing, and order auditing, providing a robust foundation for modern web engineering."
    )

    add_heading_2(doc, "8.2 Future Enhancements & Roadmap")
    add_bullet_p(doc, "Integrate Razorpay or Stripe for real-time UPI, credit card, and net-banking checkouts.", bold_prefix="1. Payment Gateway Integration: ")
    add_bullet_p(doc, "Incorporate Twilio SMS and Nodemailer email triggers for automated order dispatch notifications.", bold_prefix="2. Automated Email & SMS Alerts: ")
    add_bullet_p(doc, "Allow verified buyers to write detailed text reviews and submit 5-star ratings for hardware items.", bold_prefix="3. Rating & Review System: ")
    add_bullet_p(doc, "Implement dark/light mode toggles, discount coupon codes, and wishlist bookmarking.", bold_prefix="4. Enhanced UX & Coupons: ")

    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 9: REFERENCES & BIBLIOGRAPHY")
    
    add_heading_2(doc, "9.1 Academic Textbooks & Publications")
    add_bullet_p(doc, "Duckett, J. (2014). JavaScript and JQuery: Interactive Front-End Web Development. John Wiley & Sons.", bold_prefix="[1] Front-End Engineering: ")
    add_bullet_p(doc, "Banks, A., & Porcello, E. (2020). Learning React: Modern Patterns for Developing React Apps (2nd ed.). O'Reilly Media.", bold_prefix="[2] React Architecture: ")
    add_bullet_p(doc, "Herron, D. (2020). Node.js Web Development: Server-side development with Node 14 and Express. Packt Publishing.", bold_prefix="[3] Server-Side JavaScript: ")
    add_bullet_p(doc, "Bradshaw, S., Brazil, E., & Chodorow, K. (2019). MongoDB: The Definitive Guide (3rd ed.). O'Reilly Media.", bold_prefix="[4] NoSQL Database Design: ")

    add_heading_2(doc, "9.2 Official Web Documentation & Online Resources")
    add_bullet_p(doc, "Meta Open Source. (2024). React Official Documentation. https://react.dev/", bold_prefix="[5] React Documentation: ")
    add_bullet_p(doc, "Vite Core Team. (2024). Vite — Next Generation Frontend Tooling. https://vitejs.dev/", bold_prefix="[6] Vite Documentation: ")
    add_bullet_p(doc, "Express.js Foundation. (2024). Express — Fast, unopinionated, minimalist web framework. https://expressjs.com/", bold_prefix="[7] Express.js Guide: ")
    add_bullet_p(doc, "MongoDB Inc. (2024). MongoDB 8.0 Manual and Aggregation Pipeline Documentation. https://www.mongodb.com/docs/", bold_prefix="[8] MongoDB Manual: ")
    add_bullet_p(doc, "Mozilla Developer Network. (2024). MDN Web Docs for HTML5, CSS3, and JavaScript APIs. https://developer.mozilla.org/", bold_prefix="[9] MDN Web Docs: ")

    doc.save(output_filename)
    print(f"SUCCESS: GameKart Documentation report saved to {output_filename}")

if __name__ == "__main__":
    build_final_project_documentation()
