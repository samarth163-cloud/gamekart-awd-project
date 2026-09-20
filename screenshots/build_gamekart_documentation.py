"""
Self-Contained Generator for GAMEKART & BOOKSTORE E-COMMERCE PLATFORM
TYBCA Minor Project Documentation Report (DOCX)
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
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_DARK
    return p

def add_body_p(doc, text, bold_prefix="", space_after=3.5, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_DARK
        
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    run.font.italic = italic
    run.font.color.rgb = COLOR_TEXT
    return p

def add_bullet_p(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_DARK
        
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10.5)
    run.font.color.rgb = COLOR_TEXT
    return p

def add_figure_image(doc, img_path, caption, width_in=5.4, space_after=4):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(4)
    p_img.paragraph_format.space_after = Pt(2)
    p_img.paragraph_format.keep_with_next = True
    
    image_added = False
    if os.path.exists(img_path):
        try:
            run = p_img.add_run()
            run.add_picture(img_path, width=Inches(width_in))
            image_added = True
        except Exception:
            pass
    
    if not image_added:
        run = p_img.add_run(f"[{caption} - Screenshot to be inserted manually]")
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.italic = True
        
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(space_after)
    p_cap.paragraph_format.keep_with_next = False
    
    run_cap = p_cap.add_run(caption)
    run_cap.font.name = 'Times New Roman'
    run_cap.font.size = Pt(10)
    run_cap.font.bold = True
    run_cap.font.italic = True
    run_cap.font.color.rgb = COLOR_SECONDARY
    return p_cap

def add_styled_table(doc, headers, data, col_widths=None, font_size=9.0):
    tbl = doc.add_table(rows=len(data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_borders(tbl)
    prevent_row_split(tbl)
    make_table_header_repeat(tbl)
    
    hdr_row = tbl.rows[0]
    for idx, heading in enumerate(headers):
        cell = hdr_row.cells[idx]
        cell.text = heading
        set_cell_background(cell, HEX_PRIMARY)
        set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(font_size)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            
    for r_idx, row_data in enumerate(data):
        row = tbl.rows[r_idx + 1]
        bg_color = HEX_ZEBRA if (r_idx % 2 == 1) else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.text = str(val)
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=90, bottom=90, left=130, right=130)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            if c_idx == 0 or len(str(val)) < 8:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(font_size - 0.5)
                r.font.color.rgb = COLOR_TEXT
                
    if col_widths:
        for row in tbl.rows:
            for c_idx, w in enumerate(col_widths):
                row.cells[c_idx].width = Inches(w)
                
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(0)
    p_sp.paragraph_format.space_after = Pt(4)
    return tbl

def build_gamekart_report(output_filename="GAMEKART_TYBCA_MINOR_PROJECT_DOCUMENTATION.docx"):
    print("Building GameKart Documentation...")
    doc = docx.Document()
    
    # 1. Page Setup (A4, 1.0 inch margins)
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run('GameKart E-Commerce Platform | TYBCA Minor Project')
        hrun.font.name = 'Times New Roman'
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = COLOR_MUTED
        
        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        frun1 = fp.add_run('C. B. Patel Computer College, Surat  |  Page ')
        frun1.font.name = 'Times New Roman'
        frun1.font.size = Pt(9)
        frun1.font.color.rgb = COLOR_MUTED
        
        frun2 = fp.add_run()
        frun2.font.name = 'Times New Roman'
        frun2.font.size = Pt(9)
        frun2.font.bold = True
        frun2.font.color.rgb = COLOR_PRIMARY
        add_page_number_to_run(frun2)

    # -------------------------------------------------------------
    # PAGE 1: COVER PAGE
    # -------------------------------------------------------------
    p_col = doc.add_paragraph()
    p_col.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_col.paragraph_format.space_before = Pt(4)
    p_col.paragraph_format.space_after = Pt(2)
    
    r1 = p_col.add_run("C. B. PATEL COMPUTER COLLEGE\n& J. N. M. PATEL SCIENCE COLLEGE\n")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(15)
    r1.font.bold = True
    r1.font.color.rgb = COLOR_PRIMARY
    
    r2 = p_col.add_run("Affiliated to Veer Narmad South Gujarat University (VNSGU), Surat\nDepartment of Computer Applications")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(10.5)
    r2.font.italic = True
    r2.font.color.rgb = COLOR_MUTED

    # Logo
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(12)
    p_logo.paragraph_format.space_after = Pt(12)
    logo_path = "extracted_media/image1.png"
    if not os.path.exists(logo_path):
        logo_path = "client/src/assets/logo3.png"
    if os.path.exists(logo_path):
        r_logo = p_logo.add_run()
        r_logo.add_picture(logo_path, width=Inches(1.5))
        
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(2)
    
    rt = p_title.add_run("GAMEKART\n")
    rt.font.name = 'Times New Roman'
    rt.font.size = Pt(24)
    rt.font.bold = True
    rt.font.color.rgb = COLOR_PRIMARY
    
    rt_sub = p_title.add_run("“Full-Stack E-Commerce & Gaming Merchandise Store”\n")
    rt_sub.font.name = 'Times New Roman'
    rt_sub.font.size = Pt(12)
    rt_sub.font.bold = True
    rt_sub.font.italic = True
    rt_sub.font.color.rgb = COLOR_SECONDARY
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(8)
    p_sub.paragraph_format.space_after = Pt(4)
    
    r_rep = p_sub.add_run("A MINOR PROJECT REPORT ON\n")
    r_rep.font.name = 'Times New Roman'
    r_rep.font.size = Pt(11)
    r_rep.font.bold = True
    r_rep.font.color.rgb = COLOR_DARK
    
    r_proj = p_sub.add_run("“Dual-Portal Full-Stack E-Commerce Web Platform (Client & Admin)”\n")
    r_proj.font.name = 'Times New Roman'
    r_proj.font.size = Pt(13)
    r_proj.font.bold = True
    r_proj.font.color.rgb = COLOR_PRIMARY
    
    r_deg = p_sub.add_run("\nSubmitted in partial fulfilment of the requirements for the award of the degree of\n")
    r_deg.font.name = 'Times New Roman'
    r_deg.font.size = Pt(10)
    r_deg.font.italic = True
    
    r_bca = p_sub.add_run("BACHELOR OF COMPUTER APPLICATIONS (BCA)\n(TYBCA – SEMESTER VI: AWD & WFS COURSES)")
    r_bca.font.name = 'Times New Roman'
    r_bca.font.size = Pt(11.5)
    r_bca.font.bold = True
    r_bca.font.color.rgb = COLOR_PRIMARY

    # Student & Guide Table
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(12)
    p_sp.paragraph_format.space_after = Pt(4)
    
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, color="FFFFFF", sz="0", val="none")
    tbl.rows[0].cells[0].width = Inches(3.1)
    tbl.rows[0].cells[1].width = Inches(3.1)
    
    p_l = tbl.rows[0].cells[0].paragraphs[0]
    p_l.alignment = WD_ALIGN_PARAGRAPH.LEFT
    rl_h = p_l.add_run("SUBMITTED BY:\n")
    rl_h.font.name = 'Times New Roman'
    rl_h.font.size = Pt(10.5)
    rl_h.font.bold = True
    rl_h.font.color.rgb = COLOR_PRIMARY
    
    rl_s = p_l.add_run("Student Name: [Student Name]\nRoll No: [Roll Number]\nExam Seat No: [Seat Number]\nTYBCA Semester VI")
    rl_s.font.name = 'Times New Roman'
    rl_s.font.size = Pt(9.5)
    rl_s.font.bold = True
    rl_s.font.color.rgb = COLOR_DARK
    
    p_r = tbl.rows[0].cells[1].paragraphs[0]
    p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    rr_h = p_r.add_run("PROJECT GUIDANCE:\n")
    rr_h.font.name = 'Times New Roman'
    rr_h.font.size = Pt(10.5)
    rr_h.font.bold = True
    rr_h.font.color.rgb = COLOR_PRIMARY
    
    rr_g = p_r.add_run("Internal Guide:\n[Internal Guide Teacher]\nAsst. Professor, Dept. of Computer Applications\n\nHead of Department:\n[Head of Department]\nDept. of Computer Applications")
    rr_g.font.name = 'Times New Roman'
    rr_g.font.size = Pt(9.5)
    rr_g.font.color.rgb = COLOR_DARK

    p_foot = doc.add_paragraph()
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_foot.paragraph_format.space_before = Pt(20)
    p_foot.paragraph_format.space_after = Pt(0)
    rf = p_foot.add_run("DEPARTMENT OF COMPUTER APPLICATIONS\nACADEMIC YEAR: 2025–2026 | SURAT, GUJARAT, INDIA")
    rf.font.name = 'Times New Roman'
    rf.font.size = Pt(10)
    rf.font.bold = True
    rf.font.color.rgb = COLOR_PRIMARY

    # -------------------------------------------------------------
    # PAGE 2: COMPLETION CERTIFICATE
    # -------------------------------------------------------------
    doc.add_page_break()
    p_col = doc.add_paragraph()
    p_col.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_col.paragraph_format.space_before = Pt(10)
    p_col.paragraph_format.space_after = Pt(2)
    
    r1 = p_col.add_run("C. B. PATEL COMPUTER COLLEGE\n& J. N. M. PATEL SCIENCE COLLEGE\n")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(14)
    r1.font.bold = True
    r1.font.color.rgb = COLOR_PRIMARY
    
    r2 = p_col.add_run("Affiliated to Veer Narmad South Gujarat University (VNSGU), Surat\nDepartment of Computer Applications\n")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(11)
    r2.font.italic = True
    r2.font.color.rgb = COLOR_MUTED
    
    p_cert = doc.add_paragraph()
    p_cert.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert.paragraph_format.space_before = Pt(14)
    p_cert.paragraph_format.space_after = Pt(14)
    rc = p_cert.add_run("MINOR PROJECT COMPLETION CERTIFICATE")
    rc.font.name = 'Times New Roman'
    rc.font.size = Pt(15)
    rc.font.bold = True
    rc.font.color.rgb = COLOR_PRIMARY
    
    p_body = doc.add_paragraph()
    p_body.paragraph_format.space_before = Pt(6)
    p_body.paragraph_format.space_after = Pt(10)
    p_body.paragraph_format.line_spacing = 1.25
    p_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    p_body.add_run("This is to certify that the Minor Project entitled ")
    r_t = p_body.add_run("“GAMEKART & BOOKSTORE E-COMMERCE PLATFORM”")
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_PRIMARY
    p_body.add_run(" has been successfully designed, developed, and completed by ")
    r_st = p_body.add_run("[Student Name / Team Members]")
    r_st.font.bold = True
    p_body.add_run(", bonafide student(s) of ")
    r_deg = p_body.add_run("Third Year Bachelor of Computer Applications (TYBCA – Semester VI)")
    r_deg.font.bold = True
    p_body.add_run(" at C. B. Patel Computer College, affiliated to Veer Narmad South Gujarat University, Surat, in partial fulfilment of the requirements for the award of the degree of Bachelor of Computer Applications during the Academic Year 2025–2026.\n\nThis project represents an authentic record of independent full-stack web development carried out under the guidance and supervision of the Department faculty.")
    
    p_sig_sp = doc.add_paragraph()
    p_sig_sp.paragraph_format.space_before = Pt(36)
    
    tbl_sig = doc.add_table(rows=2, cols=3)
    tbl_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_sig, color="FFFFFF", sz="0", val="none")
    for row in tbl_sig.rows:
        row.cells[0].width = Inches(2.1)
        row.cells[1].width = Inches(2.1)
        row.cells[2].width = Inches(2.1)
        
    sigs = [
        ("___________________________", "[Internal Guide Teacher]\nInternal Guide\nDept. of Computer Applications"),
        ("___________________________", "[Head of Department]\nHead of Department\nDept. of Computer Applications"),
        ("___________________________", "[External Examiner]\nExternal Examiner\nAppointed by VNSGU")
    ]
    for idx, (line, text) in enumerate(sigs):
        c1 = tbl_sig.rows[0].cells[idx]
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p1.add_run(line)
        r.font.bold = True
        
        c2 = tbl_sig.rows[1].cells[idx]
        p2 = c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r2 = p2.add_run(text)
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = COLOR_DARK
        
    p_date = doc.add_paragraph()
    p_date.paragraph_format.space_before = Pt(30)
    rd = p_date.add_run("Date: _____________________\nPlace: Surat, Gujarat, India")
    rd.font.bold = True

    # -------------------------------------------------------------
    # PAGE 3: INDEX / TABLE OF CONTENTS
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "TABLE OF CONTENTS / INDEX")
    
    gk_toc = [
        ("1", "Minor Project Completion Certificate", "2"),
        ("2", "Table of Contents / Index", "3"),
        ("3", "Chapter 1: Introduction & Project Background", "4 - 6"),
        ("", "  1.1 Project Background & E-Commerce Context", "4"),
        ("", "  1.2 Existing Traditional Retail & Limitations", "4"),
        ("", "  1.3 Comparative Analysis: Legacy vs GameKart", "5"),
        ("", "  1.4 Problem Statement & Core Objectives", "5"),
        ("", "  1.5 Proposed Dual-Portal Solution", "5"),
        ("", "  1.6 Project Scope & Target Audience", "6"),
        ("", "  1.7 Feasibility Study (Technical, Operational, Economic)", "6"),
        ("4", "Chapter 2: Technology Used & System Requirements", "7 - 9"),
        ("", "  2.1 Frontend Architecture (React 19, Vite, Bootstrap, CSS)", "7"),
        ("", "  2.2 Backend Architecture (Node.js, Express.js APIs)", "7"),
        ("", "  2.3 Database Management (MongoDB Community, Mongoose ODM)", "8"),
        ("", "  2.4 File Upload Pipeline (Multer Disk Storage)", "8"),
        ("", "  2.5 Technology Stack Summary Table", "9"),
        ("", "  2.6 Hardware & Software Requirements", "9"),
        ("5", "Chapter 3: Objectives & Requirements Specification", "10 - 12"),
        ("", "  3.1 Primary & Secondary Objectives", "10"),
        ("", "  3.2 Measurable Success Criteria", "10"),
        ("", "  3.3 Module-wise Functional Objectives", "11"),
        ("", "  3.4 Non-Functional Requirements Specification", "11"),
        ("", "  3.5 Functional Requirements (FR-01 to FR-10)", "12"),
        ("6", "Chapter 4: System Flow Chart & Architecture", "13 - 17"),
        ("", "  4.1 System Flow Chart & Operational Flow", "13"),
        ("", "  4.2 Admin Product & Order Management Flow", "14"),
        ("", "  4.3 Use Case Diagram & Actor Matrix", "15"),
        ("", "  4.4 Data Flow Diagrams (DFD Level 0 & Level 1)", "16"),
        ("", "  4.5 Multi-Tier Client-Server Architecture", "17"),
        ("7", "Chapter 5: Database Design & Data Dictionary", "18 - 21"),
        ("", "  5.1 Database Overview & MongoDB Schema Design", "18"),
        ("", "  5.2 Entity Relationship (ER) / Schema Diagram", "18"),
        ("", "  5.3 Complete Data Dictionaries (Admins, Products, Registers, Carts)", "19 - 20"),
        ("", "  5.4 MongoDB Aggregation Pipeline ($lookup Lookups)", "21"),
        ("8", "Chapter 6: Detailed Module Specifications", "22 - 25"),
        ("", "  6.1 Client Authentication & Registration Module", "22"),
        ("", "  6.2 Product Catalog & Real-Time Search Engine", "22"),
        ("", "  6.3 Shopping Cart & Order Processing Engine", "23"),
        ("", "  6.4 User Order History & Profile Management", "23"),
        ("", "  6.5 Admin Product Inventory & Image Upload", "24"),
        ("", "  6.6 Admin Order Management & Joined Aggregations", "24"),
        ("", "  6.7 Admin User Registry & Account Oversight", "25"),
        ("9", "Chapter 7: User Interface & Screen Shots", "26 - 31"),
        ("", "  7.1 Customer Store UI Walkthrough", "26 - 28"),
        ("", "  7.2 Admin Portal UI Walkthrough", "29 - 31"),
        ("10", "Chapter 8: Software Testing & Quality Assurance", "32 - 33"),
        ("11", "Chapter 9: Platform Security Architecture", "34"),
        ("12", "Chapter 10: Future Enhancements, Conclusion & References", "35")
    ]
    add_styled_table(doc, ["Sr. No.", "Section / Topic Title", "Page No."], gk_toc, col_widths=[0.8, 4.6, 0.9], font_size=8.5)

    # -------------------------------------------------------------
    # CHAPTER 1: INTRODUCTION (PAGES 4 - 6)
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 1: INTRODUCTION")
    add_heading_2(doc, "1.1 Project Background & E-Commerce Context")
    add_body_p(
        doc,
        "The digital economy has fundamentally reshaped how consumers explore, evaluate, and purchase retail goods. Specialized e-commerce sectors, particularly gaming hardware, consoles, interactive accessories, and specialized literature, demand dynamic platforms that provide instantaneous catalog discovery, clear product specifications, high-resolution imagery, and straightforward order placement. GameKart is engineered as a robust, full-stack dual-portal web application built on the MERN technology stack, comprising an independent Customer Shopping Store and an Administrative Management Dashboard."
    )
    
    add_heading_2(doc, "1.2 Existing Traditional Retail & Limitations")
    add_body_p(doc, "Traditional retail commerce and early web storefronts suffer from multiple operational limitations:")
    add_bullet_p(doc, "Manual inventory tracking prone to stock mismatches and delayed updates.", bold_prefix="1. Inefficient Inventory Control: ")
    add_bullet_p(doc, "Customers lack real-time visibility into available hardware stocks and dynamic pricing.", bold_prefix="2. Poor Customer Transparency: ")
    add_bullet_p(doc, "Monolithic server rendering creates sluggish page updates and poor mobile usability.", bold_prefix="3. High Latency: ")

    doc.add_page_break()
    add_heading_2(doc, "1.3 Comparative Analysis: Legacy Systems vs. GameKart")
    gk_comp = [
        ["Feature / Dimension", "Legacy Retail / Static Store", "GameKart Modern Web Platform"],
        ["Client Experience", "Static HTML reloads on every click", "Single Page App (React 19) with instant search"],
        ["Admin Controls", "Manual database entry / Desktop spreadsheets", "Dedicated web admin dashboard with image uploads"],
        ["Image Processing", "Manual FTP server file transfer", "Automated Multer multipart disk storage pipeline"],
        ["Order Management", "Paper receipts or delayed manual batching", "Instant MongoDB cart state machine & live aggregations"],
        ["Database Architecture", "Traditional tabular SQL with rigid migrations", "Flexible MongoDB NoSQL document collections"],
        ["REST API Decoupling", "Tightly coupled server-rendered monolithic code", "Modular Express.js REST APIs (Ports 4000 & 5000)"]
    ]
    add_styled_table(doc, ["Dimension", "Legacy Storefront", "GameKart Platform"], gk_comp, col_widths=[1.5, 2.3, 2.5], font_size=8.5)

    add_heading_2(doc, "1.4 Problem Statement & Core Objectives")
    add_body_p(
        doc,
        "Modern digital consumers require fluid, responsive web experiences with live search capabilities, instant cart additions, transparent order tracking, and reliable image viewing. Simultaneously, administrators need a centralized portal to add products with image uploads, update catalogue prices, audit registered user accounts, and track customer purchases. GameKart addresses this challenge by providing two dedicated portals communicating with separate REST APIs."
    )

    doc.add_page_break()
    add_heading_2(doc, "1.5 Proposed Dual-Portal Solution")
    add_body_p(
        doc,
        "GameKart implements a two-tier frontend architecture powered by React 19 and Vite: (1) Customer Store (`http://localhost:5174/`): Enables visitors to browse catalogues, search products by keyword, view product specifications, register accounts with avatar uploads, add items to cart, and place orders; and (2) Admin Portal (`http://localhost:5173/`): Provides administrative tools to upload products with images via Multer, update product details, delete obsolete stock, view real-time customer orders with joined details, and monitor registered users."
    )

    add_heading_2(doc, "1.6 Project Scope & Feasibility Study")
    add_bullet_p(doc, "MERN stack is mature and fully open-source with rapid local execution.", bold_prefix="Technical Feasibility: ")
    add_bullet_p(doc, "Zero software licensing expense; built using Node.js, Express, MongoDB Community, and React.", bold_prefix="Economic Feasibility: ")
    add_bullet_p(doc, "Intuitive user interface styled with modern Bootstrap and responsive CSS.", bold_prefix="Operational Feasibility: ")

    # -------------------------------------------------------------
    # CHAPTER 2: TECHNOLOGY USED (PAGES 7 - 9)
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 2: TECHNOLOGY USED & REQUIREMENTS")
    add_heading_2(doc, "2.1 Frontend Architecture (React 19, Vite, Bootstrap)")
    add_bullet_p(doc, "Latest React release offering concurrent rendering, component state management, and virtual DOM efficiency.", bold_prefix="React.js (v19.1): ")
    add_bullet_p(doc, "High-performance build tooling with lightning-fast HMR and Rollup bundling.", bold_prefix="Vite (v7.1): ")
    add_bullet_p(doc, "Component framework providing responsive grid layouts, navbars, and interactive modals.", bold_prefix="Bootstrap (v5.3): ")
    add_bullet_p(doc, "Client-side routing managing seamless multi-view navigation across customer and admin portals.", bold_prefix="React Router DOM (v7.8): ")
    
    add_heading_2(doc, "2.2 Backend Architecture (Node.js, Express.js, Multer)")
    add_bullet_p(doc, "Asynchronous, event-driven JavaScript runtime powering high-throughput API endpoints.", bold_prefix="Node.js (v20+): ")
    add_bullet_p(doc, "Fast web framework structuring REST endpoints for authentication, products, carts, and orders.", bold_prefix="Express.js (v5.2): ")
    add_bullet_p(doc, "Multipart form-data middleware handling multipart image uploads to `/uploads` directory.", bold_prefix="Multer (v2.3): ")
    add_bullet_p(doc, "Cross-Origin Resource Sharing enabling smooth communication across ports 5173, 5174, 4000, and 5000.", bold_prefix="CORS Middleware: ")

    doc.add_page_break()
    add_heading_2(doc, "2.3 Database Management (MongoDB & Mongoose ODM)")
    add_bullet_p(doc, "NoSQL document database storing collections as flexible BSON records on `mongodb://localhost:27017/dbProject`.", bold_prefix="MongoDB Community 8.x: ")
    add_bullet_p(doc, "Object-Data Modeling library enforcing strict schemas, type validation, and aggregation pipelines.", bold_prefix="Mongoose (v8.24): ")
    add_bullet_p(doc, "Desktop graphical interface for inspecting collections (`admins`, `products`, `registers`, `carts`).", bold_prefix="MongoDB Compass: ")

    add_heading_2(doc, "2.4 Dual-Port Architecture & Pipeline Summary")
    add_body_p(
        doc,
        "GameKart segregates administrative duties from customer operations by operating dual backend instances: Port 5000 hosts the Admin API while Port 4000 hosts the Client API. Both communicate with the shared MongoDB database `dbProject`."
    )

    doc.add_page_break()
    add_heading_2(doc, "2.5 Technology Stack Summary Table")
    gk_tech = [
        ["Layer / Subsystem", "Technology", "Port / Host", "Role in GameKart"],
        ["Customer Frontend", "React 19 + Vite", "http://localhost:5174", "Catalog browsing, search, cart, and orders UI"],
        ["Admin Frontend", "React 19 + Vite", "http://localhost:5173", "Product management, user list, orders audit UI"],
        ["Customer Backend API", "Express 5.2 + Node.js", "http://localhost:4000", "Customer signup, login, cart, order APIs"],
        ["Admin Backend API", "Express 5.2 + Node.js", "http://localhost:5000", "Product CRUD, image upload, order lookups"],
        ["Database Server", "MongoDB 8.x", "localhost:27017", "Persistent storage for `dbProject` database"],
        ["File Uploads", "Multer DiskStorage", "/uploads directory", "Image upload storage for products and avatars"]
    ]
    add_styled_table(doc, ["Subsystem", "Technology", "Port", "Operational Role"], gk_tech, col_widths=[1.5, 1.5, 1.4, 1.9], font_size=8.0)

    add_heading_2(doc, "2.6 Hardware & Software Specifications")
    gk_hw = [
        ["Component", "Minimum Requirement", "Recommended Specification"],
        ["CPU", "Intel Core i3 Dual Core 2.0 GHz", "Intel Core i5 / AMD Ryzen 5 Quad Core 2.5+ GHz"],
        ["RAM", "4 GB DDR3/DDR4", "8 GB / 16 GB DDR4"],
        ["Storage", "2 GB Free Storage (Node Modules + DB)", "10 GB Free SSD Storage"],
        ["OS", "Windows 10 / 11 64-bit", "Windows 11 64-bit"],
        ["Browser", "Google Chrome 110+, MS Edge", "Latest Google Chrome with DevTools"]
    ]
    add_styled_table(doc, ["Component", "Minimum Requirement", "Recommended Spec"], gk_hw, col_widths=[1.5, 2.3, 2.5], font_size=8.0)

    # -------------------------------------------------------------
    # CHAPTER 3: OBJECTIVES & REQUIREMENTS (PAGES 10 - 12)
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 3: OBJECTIVES & REQUIREMENTS")
    add_heading_2(doc, "3.1 Primary & Secondary Objectives")
    add_bullet_p(doc, "Develop a responsive e-commerce web platform for gaming hardware, consoles, and books.", bold_prefix="1. Core Storefront: ")
    add_bullet_p(doc, "Implement an administrative portal allowing complete product catalog CRUD with image upload capabilities.", bold_prefix="2. Product Management: ")
    add_bullet_p(doc, "Provide a reliable cart and order state pipeline transitioning items from 'cart' to 'ordered'.", bold_prefix="3. Order Pipeline: ")
    add_bullet_p(doc, "Enable customer account registration with profile avatar uploads and secure credentials.", bold_prefix="4. User Accounts: ")

    add_heading_2(doc, "3.2 Project Success Criteria Matrix")
    gk_succ = [
        ["Evaluation Dimension", "Success Target", "Validation Method"],
        ["Product Catalog CRUD", "100% add, update, retrieve, and delete success with images", "Admin dashboard testing & DB verification"],
        ["Image Upload Pipeline", "Images saved to disk and served statically via /uploads", "File system check and browser image render"],
        ["Cart & Order Pipeline", "Items added to cart and updated to 'ordered' upon checkout", "End-to-end checkout execution"],
        ["Aggregated Order Lookup", "Admin orders view displays joined user and product info", "MongoDB $lookup aggregation validation"]
    ]
    add_styled_table(doc, ["Dimension", "Success Target", "Validation Method"], gk_succ, col_widths=[1.5, 2.7, 2.1], font_size=8.0)

    doc.add_page_break()
    add_heading_2(doc, "3.3 Module-wise Functional Objectives")
    gk_mod_obj = [
        ["Subsystem / Module", "Functional Objective"],
        ["Customer Authentication", "Allow visitors to register accounts with profile pictures and log in securely."],
        ["Product Catalog & Search", "Display gaming items and books with real-time keyword filtering and detail views."],
        ["Cart & Checkout Engine", "Manage user cart items, compute pricing, and transition items to 'ordered' status."],
        ["Admin Inventory Manager", "Provide multipart form for adding products with image uploads and editing price/description."],
        ["Admin Order Monitor", "Execute MongoDB aggregate lookups joining user details and product data for each order."],
        ["Admin User Directory", "Display all registered customers with name, email, gender, city, and profile picture."]
    ]
    add_styled_table(doc, ["Module", "Functional Objective"], gk_mod_obj, col_widths=[2.0, 4.3], font_size=8.5)

    add_heading_2(doc, "3.4 Non-Functional Requirements Specification")
    gk_nfr = [
        ["Quality Attribute", "Specification & Requirement"],
        ["Performance", "API response times < 150ms for product queries and order insertions."],
        ["Security", "Role separation between admin endpoints (Port 5000) and client endpoints (Port 4000)."],
        ["Usability", "Responsive Bootstrap styling adapting to desktop, tablet, and mobile viewports."],
        ["Reliability", "Graceful handling of missing images and invalid database queries with proper HTTP status codes."]
    ]
    add_styled_table(doc, ["Attribute", "Specification"], gk_nfr, col_widths=[1.8, 4.5], font_size=8.5)

    doc.add_page_break()
    add_heading_2(doc, "3.5 Functional Requirements (FR-01 to FR-10)")
    gk_fr = [
        ["Req ID", "Requirement Title", "Description"],
        ["FR-01", "Customer Registration", "Allow new users to register with name, email, password, gender, city, and avatar."],
        ["FR-02", "Customer Login", "Authenticate customers against `registers` collection and store session state."],
        ["FR-03", "Product Browsing", "Fetch and display all active products from `products` collection."],
        ["FR-04", "Product Search", "Filter product cards dynamically based on user search input."],
        ["FR-05", "Product Details", "Render comprehensive product view with high-res image and description."],
        ["FR-06", "Add to Cart", "Insert item into `carts` collection with status 'cart'."],
        ["FR-07", "Place Order", "Update cart items to status 'ordered' and record order timestamp."],
        ["FR-08", "Admin Add Product", "Upload product image via Multer and save record to `products` collection."],
        ["FR-09", "Admin Update Product", "Update product name, description, and price via PUT endpoint."],
        ["FR-10", "Admin Order Aggregation", "Join `carts`, `registers`, and `products` via $lookup to display orders."]
    ]
    add_styled_table(doc, ["ID", "Title", "Functional Description"], gk_fr, col_widths=[0.8, 1.8, 3.7], font_size=8.5)

    # -------------------------------------------------------------
    # CHAPTER 4: SYSTEM DESIGN & FLOW CHARTS (PAGES 13 - 17)
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 4: SYSTEM FLOW CHART & ARCHITECTURE")
    add_heading_2(doc, "4.1 System Flow Chart & Operational Flow")
    add_body_p(
        doc,
        "The GameKart operational workflow traces customer interactions from account registration and product discovery to cart checkout, alongside administrative inventory and order management."
    )
    
    gk_flow_steps = [
        ["Step", "Phase", "Operational Description"],
        ["1", "Visitor Entry", "Visitor opens GameKart Customer Store at `http://localhost:5174/`."],
        ["2", "Authentication", "User signs up with avatar upload or logs in with registered email/password."],
        ["3", "Catalog Discovery", "User browses gaming products/books and utilizes live search bar."],
        ["4", "Item Selection", "User inspects product details and clicks 'Add to Cart'."],
        ["5", "Cart & Checkout", "User views cart and clicks 'Order Now', updating cart status to 'ordered'."],
        ["6", "Admin Processing", "Admin logs in at `http://localhost:5173/`, audits incoming orders, and adds new products."]
    ]
    add_styled_table(doc, ["Step", "Phase", "Description"], gk_flow_steps, col_widths=[0.7, 1.8, 3.8], font_size=8.5)

    doc.add_page_break()
    add_heading_2(doc, "4.2 Admin Product & Order Workflow")
    add_body_p(
        doc,
        "The Admin workflow enables store managers to maintain the product inventory and fulfill customer orders. Products uploaded via Multer are stored in the local disk directory and registered in MongoDB with their filename, price, and description."
    )
    
    add_heading_2(doc, "4.3 Use Case Specifications")
    gk_uc = [
        ["Actor", "Use Case", "Description"],
        ["Customer", "Register & Login", "Create account with profile picture and authenticate session."],
        ["Customer", "Search & Browse Products", "View gaming hardware catalog with live search filter."],
        ["Customer", "Manage Cart & Order", "Add items to cart, view total cost, and confirm order placement."],
        ["Admin", "Manage Product Inventory", "Create new products with image upload, edit prices, delete items."],
        ["Admin", "View Joined Orders", "Inspect customer orders with joined user profile and product image."],
        ["Admin", "Audit Registered Users", "Browse complete registry of customer accounts and cities."]
    ]
    add_styled_table(doc, ["Actor", "Use Case", "Description"], gk_uc, col_widths=[1.2, 2.0, 3.1], font_size=8.5)

    doc.add_page_break()
    add_heading_2(doc, "4.4 Data Flow Diagrams (DFD Level 0 & Level 1)")
    add_body_p(
        doc,
        "In DFD Level 0 (Context Diagram), the Customer provides registration credentials, search keywords, and order actions, receiving product data, cart totals, and order confirmations. The Administrator supplies product uploads and receives aggregate order lists and user reports."
    )
    add_body_p(
        doc,
        "In DFD Level 1, the system decomposes into: (1.0) User Management, (2.0) Product Catalog Management, (3.0) Shopping Cart & Orders, and (4.0) Admin Aggregations, reading and writing to data stores D1: `registers`, D2: `products`, D3: `carts`, and D4: `admins`."
    )

    add_heading_2(doc, "4.5 Dual-Tier Client-Server Architecture")
    add_body_p(
        doc,
        "GameKart adopts a decoupled MERN architecture where client-side applications (Vite SPAs) run on separate browser ports (5174 for Customer, 5173 for Admin) and communicate asynchronously via Axios REST requests to independent Express API servers (Port 4000 for Customer API, Port 5000 for Admin API), persisting to MongoDB on port 27017."
    )

    # -------------------------------------------------------------
    # CHAPTER 5: DATABASE DESIGN (PAGES 18 - 21)
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 5: DATABASE DESIGN & DATA DICTIONARY")
    add_heading_2(doc, "5.1 Database Overview (MongoDB `dbProject`)")
    add_body_p(
        doc,
        "GameKart uses MongoDB as its primary persistence engine under the database name `dbProject`. The schema is modeled using Mongoose across four distinct collections: `admins`, `products`, `registers`, and `carts`."
    )
    
    add_heading_2(doc, "5.2 Data Dictionary: `admins` Collection (Table 5.1)")
    gk_admin_dict = [
        ["Field Name", "Data Type", "Constraints", "Description"],
        ["_id", "ObjectId", "Primary Key, Auto", "Unique 12-byte identifier for administrator."],
        ["name", "String", "Required", "Full name of store administrator."],
        ["email", "String", "Required, Unique", "Admin email address for portal login."],
        ["password", "String", "Required", "Admin login password credential."]
    ]
    add_styled_table(doc, ["Field", "Type", "Constraints", "Description"], gk_admin_dict, col_widths=[1.2, 1.0, 1.8, 2.3], font_size=8.0)

    doc.add_page_break()
    add_heading_2(doc, "5.3 Data Dictionary: `products` Collection (Table 5.2)")
    gk_prod_dict = [
        ["Field Name", "Data Type", "Constraints", "Description"],
        ["_id", "ObjectId", "Primary Key, Auto", "Unique identifier for product item."],
        ["pname", "String", "Required", "Product title / book name (e.g. 'PS5 Console')."],
        ["pimg", "String", "Required", "Uploaded image filename stored in `/uploads`."],
        ["description", "String", "Optional", "Detailed description of gaming hardware / book."],
        ["price", "Number", "Required", "Retail price in Indian Rupees (INR)."]
    ]
    add_styled_table(doc, ["Field", "Type", "Constraints", "Description"], gk_prod_dict, col_widths=[1.2, 1.0, 1.8, 2.3], font_size=8.0)

    add_heading_2(doc, "5.4 Data Dictionary: `registers` Collection (Table 5.3)")
    gk_reg_dict = [
        ["Field Name", "Data Type", "Constraints", "Description"],
        ["_id", "ObjectId", "Primary Key, Auto", "Unique identifier for registered customer."],
        ["name", "String", "Required", "Full name of the registered customer."],
        ["email", "String", "Required, Unique", "Customer email address for store login."],
        ["password", "String", "Required", "Customer account password."],
        ["gender", "String", "Optional", "Customer gender identifier."],
        ["city", "String", "Optional", "Customer city (e.g. 'Surat')."],
        ["profile", "String", "Optional", "Uploaded avatar image filename."]
    ]
    add_styled_table(doc, ["Field", "Type", "Constraints", "Description"], gk_reg_dict, col_widths=[1.2, 1.0, 1.8, 2.3], font_size=8.0)

    doc.add_page_break()
    add_heading_2(doc, "5.5 Data Dictionary: `carts` Collection (Table 5.4)")
    gk_cart_dict = [
        ["Field Name", "Data Type", "Constraints", "Description"],
        ["_id", "ObjectId", "Primary Key, Auto", "Unique identifier for cart / order item."],
        ["order_date", "Date", "Default: Date.now", "Timestamp when item was added or ordered."],
        ["pid", "String", "Required", "String reference to product `_id`."],
        ["uid", "String", "Required", "String reference to user `_id`."],
        ["status", "String", "Default: 'cart'", "State: 'cart' (in cart) or 'ordered' (checked out)."]
    ]
    add_styled_table(doc, ["Field", "Type", "Constraints", "Description"], gk_cart_dict, col_widths=[1.2, 1.0, 1.8, 2.3], font_size=8.0)

    add_heading_2(doc, "5.6 MongoDB Aggregation Pipeline ($lookup Strategy)")
    add_body_p(
        doc,
        "To present complete order summaries in the Admin portal, Express executes a MongoDB aggregation pipeline on the `carts` collection. The pipeline matches `status: 'ordered'`, converts `uid` and `pid` string fields to ObjectIds via `$toObjectId`, and executes `$lookup` joins on `registers` and `products` to return consolidated user profile and product pricing data in a single database round-trip."
    )

    # -------------------------------------------------------------
    # CHAPTER 6: MODULE SPECIFICATIONS (PAGES 22 - 25)
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 6: DETAILED MODULE SPECIFICATIONS")
    add_heading_2(doc, "6.1 Customer Authentication & Registration Module")
    add_bullet_p(doc, "Allow new customers to sign up with avatar upload and sign in to their shopping session.", bold_prefix="Purpose: ")
    add_bullet_p(doc, "Client sends multipart form with name, email, password, gender, city, and profile picture; backend saves file and registers document.", bold_prefix="Workflow: ")
    add_bullet_p(doc, "POST /signup, POST /login on port 4000; writes to `registers` collection.", bold_prefix="Backend Endpoints: ")

    add_heading_2(doc, "6.2 Product Catalog & Search Module")
    add_bullet_p(doc, "Provide live product grid with instantaneous search filtering.", bold_prefix="Purpose: ")
    add_bullet_p(doc, "User enters keyword in search input; React state filters the products array in real time without server latency.", bold_prefix="Workflow: ")
    add_bullet_p(doc, "GET /getProducts, GET /getProducts/:id on port 4000; reads `products` collection.", bold_prefix="Backend Endpoints: ")

    doc.add_page_break()
    add_heading_2(doc, "6.3 Shopping Cart & Order Processing Engine")
    add_bullet_p(doc, "Facilitate item selection, pricing aggregation, and checkout placement.", bold_prefix="Purpose: ")
    add_bullet_p(doc, "Clicking 'Add to Cart' inserts record with `status: 'cart'`. Clicking 'Order Now' in cart view updates status to 'ordered'.", bold_prefix="Workflow: ")
    add_bullet_p(doc, "POST /addCart, GET /getCart/:id, PUT /orderNow, DELETE /delCart/:id on port 4000.", bold_prefix="Backend Endpoints: ")

    add_heading_2(doc, "6.4 User Order History Module")
    add_bullet_p(doc, "Enable customers to inspect all their past placed orders.", bold_prefix="Purpose: ")
    add_bullet_p(doc, "Displays orders matching user ID with product images, purchase date, and cancel option.", bold_prefix="Workflow: ")
    add_bullet_p(doc, "GET /orders/:id on port 4000; reads `carts` joined with `products`.", bold_prefix="Backend Endpoints: ")

    doc.add_page_break()
    add_heading_2(doc, "6.5 Admin Product Inventory & Image Upload Module")
    add_bullet_p(doc, "Empower administrators to publish new products with images and edit inventory.", bold_prefix="Purpose: ")
    add_bullet_p(doc, "Multer diskStorage saves product photo to `admin/src/uploads/`; Express writes `pname`, `pimg`, `description`, `price` to MongoDB.", bold_prefix="Workflow: ")
    add_bullet_p(doc, "POST /products, PUT /updateProducts/:id, DELETE /Delproducts/:id on port 5000.", bold_prefix="Backend Endpoints: ")

    add_heading_2(doc, "6.6 Admin Order Management & Joined Aggregation Module")
    add_bullet_p(doc, "Provide store managers an aggregated live view of all customer orders.", bold_prefix="Purpose: ")
    add_bullet_p(doc, "Fetches all carts with `status: 'ordered'`, displaying customer name, city, item image, price, and order date.", bold_prefix="Workflow: ")
    add_bullet_p(doc, "GET /orders on port 5000 using MongoDB `$lookup` aggregation.", bold_prefix="Backend Endpoints: ")

    doc.add_page_break()
    add_heading_2(doc, "6.7 Admin User Registry Module")
    add_bullet_p(doc, "Display complete directory of registered customer accounts.", bold_prefix="Purpose: ")
    add_bullet_p(doc, "Renders tabular view of all registered users with avatar, full name, email, gender, and city.", bold_prefix="Workflow: ")
    add_bullet_p(doc, "GET /users on port 5000; reads `registers` collection.", bold_prefix="Backend Endpoints: ")

    # -------------------------------------------------------------
    # CHAPTER 7: USER INTERFACE & SCREENSHOTS (PAGES 26 - 31)
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 7: USER INTERFACE & SCREEN SHOTS")
    add_heading_2(doc, "7.1 Customer Shopping Store UI (Port 5174)")
    
    client_imgs = [
        ("client/src/assets/hero-banner.jpg", "Figure 1 – Customer Store Home Page Banner & Navigation"),
        ("client/src/uploads/console-ps5.jpg", "Figure 2 – Product Catalogue Showcase: PS5 Gaming Console"),
        ("client/src/uploads/controller-rgb.jpg", "Figure 3 – Product Details View: Wireless RGB Gaming Controller"),
        ("client/src/uploads/gaming-chair.jpg", "Figure 4 – Ergonomic Pro Gaming Chair Item Card"),
        ("client/src/uploads/vr-headset.jpg", "Figure 5 – Next-Gen Virtual Reality Headset Item Card")
    ]
    for img_p, cap in client_imgs:
        if os.path.exists(img_p):
            add_figure_image(doc, img_p, cap, width_in=4.5, space_after=3)
            
    doc.add_page_break()
    add_heading_2(doc, "7.2 Admin Management Portal UI (Port 5173)")
    admin_imgs = [
        ("admin/src/assets/hero-banner.jpg", "Figure 6 – Admin Dashboard Overview & Navigation Header"),
        ("admin/src/uploads/curved-monitor.jpg", "Figure 7 – Admin Product Inventory: 4K Curved Gaming Monitor"),
        ("admin/src/uploads/keyboard-mechanical.jpg", "Figure 8 – Admin Product Inventory: Mechanical RGB Keyboard"),
        ("admin/src/uploads/stream-deck.jpg", "Figure 9 – Admin Order Review & Inventory Stream Deck Item")
    ]
    for img_p, cap in admin_imgs:
        if os.path.exists(img_p):
            add_figure_image(doc, img_p, cap, width_in=4.5, space_after=3)

    # -------------------------------------------------------------
    # CHAPTER 8: TESTING & QA (PAGES 32 - 33)
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 8: SOFTWARE TESTING & QUALITY ASSURANCE")
    add_heading_2(doc, "8.1 Testing Methodology")
    add_body_p(
        doc,
        "GameKart was rigorously evaluated using functional unit testing, REST API validation via Postman, and end-to-end black-box checkout testing."
    )
    
    add_heading_2(doc, "8.2 Comprehensive Test Cases Specification (TC-01 to TC-13)")
    gk_tests = [
        ["Test ID", "Module", "Scenario", "Input / Precondition", "Expected Result", "Status"],
        ["TC-01", "Client Auth", "User Registration", "Valid name, email, password, avatar", "200 OK; user record created in MongoDB", "Pass"],
        ["TC-02", "Client Auth", "User Login", "Registered email and password", "200 OK; login successful; ID stored", "Pass"],
        ["TC-03", "Client Auth", "Invalid Login", "Unregistered email / wrong password", "401 Unauthorized; error message displayed", "Pass"],
        ["TC-04", "Products", "Fetch Products", "GET /getProducts endpoint", "200 OK; array of all products returned", "Pass"],
        ["TC-05", "Products", "Product Search", "Type 'Controller' in search bar", "Product grid dynamically filters matching items", "Pass"],
        ["TC-06", "Cart", "Add Item to Cart", "Click 'Add to Cart' button", "200 OK; Cart item created with status 'cart'", "Pass"],
        ["TC-07", "Cart", "Place Order", "Click 'Order Now' in cart", "200 OK; Cart status updated to 'ordered'", "Pass"],
        ["TC-08", "Admin Auth", "Admin Login", "admin@gamekart.com / admin", "200 OK; redirected to admin dashboard", "Pass"],
        ["TC-09", "Admin Prod", "Add Product", "Multipart name, price, image file", "201 Created; image saved to /uploads", "Pass"],
        ["TC-10", "Admin Prod", "Update Product", "PUT /updateProducts/:id with new price", "200 OK; product price modified in MongoDB", "Pass"],
        ["TC-11", "Admin Prod", "Delete Product", "DELETE /Delproducts/:id", "200 OK; product removed from database", "Pass"],
        ["TC-12", "Admin Orders", "View Joined Orders", "GET /orders with $lookup", "200 OK; returns orders with user and product", "Pass"],
        ["TC-13", "Admin Users", "Fetch Users List", "GET /users on port 5000", "200 OK; returns all customer accounts", "Pass"]
    ]
    add_styled_table(doc, ["ID", "Module", "Scenario", "Input", "Expected Result", "Status"], gk_tests, col_widths=[0.7, 0.9, 1.3, 1.5, 1.5, 0.6], font_size=8.0)

    # -------------------------------------------------------------
    # CHAPTER 9, 10, 11 & REFERENCES (PAGES 34 - 35)
    # -------------------------------------------------------------
    doc.add_page_break()
    add_heading_1(doc, "CHAPTER 9: PLATFORM SECURITY ARCHITECTURE")
    add_bullet_p(doc, "Dual-port separation isolates admin operations on Port 5000 from client operations on Port 4000.", bold_prefix="1. Port Isolation: ")
    add_bullet_p(doc, "Multer disk storage sanitizes uploaded filenames, enforcing lowercase extensions and isolated directory storage.", bold_prefix="2. Upload Sanitization: ")
    add_bullet_p(doc, "CORS middleware restricts API access to authorized frontend origins.", bold_prefix="3. CORS Protection: ")

    add_heading_1(doc, "CHAPTER 10: FUTURE ENHANCEMENTS & CONCLUSION")
    add_heading_2(doc, "10.1 Future Enhancements")
    add_bullet_p(doc, "Integration of live online payment gateways (Razorpay / Stripe) for instant debit/credit card checkouts.", bold_prefix="Payment Gateway: ")
    add_bullet_p(doc, "Automated SMS/Email notifications for order confirmation and shipment tracking.", bold_prefix="Order Alerts: ")
    add_bullet_p(doc, "Customer product reviews and 5-star rating system.", bold_prefix="Reviews & Ratings: ")

    add_heading_2(doc, "10.2 Conclusion")
    add_body_p(
        doc,
        "The GameKart & Bookstore E-Commerce Platform successfully demonstrates the implementation of a full-stack MERN application. It delivers a fast, responsive customer storefront alongside an intuitive management dashboard, demonstrating proficiency in React, Node.js, Express, and MongoDB."
    )

    add_heading_1(doc, "CHAPTER 11: REFERENCES & BIBLIOGRAPHY")
    add_bullet_p(doc, "React Documentation. (2024). React 19 Docs. https://react.dev/", bold_prefix="[1] React.js: ")
    add_bullet_p(doc, "Node.js Foundation. (2024). Node.js v20 LTS Documentation. https://nodejs.org/", bold_prefix="[2] Node.js: ")
    add_bullet_p(doc, "Express.js Core Team. (2024). Express Framework Guide. https://expressjs.com/", bold_prefix="[3] Express.js: ")
    add_bullet_p(doc, "MongoDB Inc. (2024). MongoDB 8.0 Manual & Aggregation Pipeline. https://www.mongodb.com/docs/", bold_prefix="[4] MongoDB: ")
    add_bullet_p(doc, "Bootstrap Team. (2024). Bootstrap v5.3 Framework. https://getbootstrap.com/", bold_prefix="[5] Bootstrap: ")

    doc.save(output_filename)
    print(f"SUCCESS: GameKart Documentation saved to {output_filename}")

if __name__ == "__main__":
    build_gamekart_report()
