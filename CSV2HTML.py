import csv

#CHI
with open('CHI.csv', 'r',) as input, open('output.txt', 'w', newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"CHI\">CHI</a></td></thead>");
    for row in reader:
        #print(row)
        output.write("<tr>")
        output.write("<td rowspan=1>"+ row[0]+ "</td>" + "<td><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td>" + row[2] + "</td>")
        output.write("</tr>")
    output.write("</table>");
    output.write("<br>")

#UbiComp
with open('UbiComp.csv', 'r',) as input, open('output.txt', 'a', newline='') as output:
    reader = csv.reader(input, delimiter = ',')

    output.write("<table><thead><td colspan=3><a name=\"UbiComp\">UbiComp/Pervasive/IMWUT</a></td></thead>");
    for row in reader:
        #print(row)
        output.write("<tr>")
        output.write("<td rowspan=1>"+ row[0]+ "</td>" + "<td><a href=\"" + row[3] + "\">" + row[1] + "</a></td>" + "<td>" + row[2] + "</td>")
        output.write("</tr>")
    output.write("</table>");
    output.write("<br>")
