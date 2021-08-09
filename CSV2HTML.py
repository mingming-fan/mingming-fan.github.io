import csv


#CHI
with open('CHI.csv', 'r', encoding='gbk') as input, open('CHI.txt', 'w', newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"CHI\">CHI</a></td></thead>");
    counter = 1
    for row in reader:
        #print(row)
        if counter == 1:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%>" + row[1] + "</td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        else:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        counter = counter + 1
    output.write("</table>");
    output.write("<br>")


#VIS
with open('VIS.csv', 'r', encoding='gbk') as input, open('VIS.txt', 'w', newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"VIS\">VIS (InfoVis, VAST, SciVis)</a></td></thead>");
    counter = 1
    for row in reader:
        #print(row)
        if counter == 1:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%>" + row[1] + "</td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        else:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        counter = counter + 1
    output.write("</table>");
    output.write("<br>")

#UbiComp
with open('UbiComp.csv', 'r', encoding='gbk') as input, open('UbiComp.txt', 'w', newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"UbiComp\">UbiComp/Pervasive/IMWUT</a></td></thead>");
    counter = 1
    for row in reader:
        if counter == 1:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%>" + row[1] + "</td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        else:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        counter = counter + 1
    output.write("</table>");
    output.write("<br>")


#CSCW
with open('CSCW.csv', 'r', encoding='gb18030', errors='ignore') as input, open('CSCW.txt', 'w',newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"CSCW\">CSCW/PACMHCI</a></td></thead>");
    counter = 1
    for row in reader:
        #print(row)
        if counter == 1:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%>" + row[1] + "</td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        else:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        counter = counter + 1
    output.write("</table>");
    output.write("<br>")


#UIST
with open('UIST.csv', 'r', encoding='gb18030', errors='ignore') as input, open('UIST.txt', 'w', newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"UIST\">UIST</a></td></thead>");
    counter = 1
    for row in reader:
        #print(row)
        if counter == 1:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%>" + row[1] + "</td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        else:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        counter = counter + 1
    output.write("</table>");
    output.write("<br>")

#IUI
with open('IUI.csv', 'r', encoding='gb18030', errors='ignore') as input, open('IUI.txt', 'w', newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"IUI\">IUI</a></td></thead>");
    counter = 1
    for row in reader:
        #print(row)
        if counter == 1:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%>" + row[1] + "</td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        else:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        counter = counter + 1
    output.write("</table>");
    output.write("<br>")

#DIS
with open('DIS.csv', 'r', encoding='gb18030', errors='ignore') as input, open('DIS.txt', 'w', newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"DIS\">DIS</a></td></thead>");
    counter = 1
    for row in reader:
        #print(row)
        if counter == 1:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%>" + row[1] + "</td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        else:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        counter = counter + 1
    output.write("</table>");
    output.write("<br>")


#ASSETS
with open('ASSETS.csv', 'r', encoding='gb18030', errors='ignore') as input, open('ASSETS.txt', 'w', newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"ASSETS\">ASSETS</a></td></thead>");
    counter = 1
    for row in reader:
        #print(row)
        if counter == 1:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%>" + row[1] + "</td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        else:
            output.write("<tr>")
            output.write("<td width=2.5%>"+ row[0]+ "</td>" + "<td width=37.5%><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td width=60%>" + row[2] + "</td>")
            output.write("</tr>")
        counter = counter + 1
    output.write("</table>");
    output.write("<br>")
