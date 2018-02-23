import re
import os, errno
import csv

def indexmaker( foldername,filename ):
    ### Input Parameters ###########################################################################################
    infile = foldername + '/' + filename + '.svg'
    try:
        os.makedirs(foldername + '/' + filename)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
            
    outfile_name = foldername + '/' + filename + '/index.html'
    
    ################################################################################################################
    
    table = open( foldername + '/' +'Labels.csv', 'r'  ).readlines()
    tab = []
    
    for line in table:
        sline = line.strip().split(',')
        tab.append(sline)
    
    
    prog = re.compile('path id=.*?" ')
    
    lines = open(infile, 'r').readlines()
    o = open(outfile_name, 'w')
    
    #############################################################################################################
    for x in range(len(lines)):
        if (lines[x][0]+lines[x][1]+lines[x][2]+lines[x][3] == 'view') and (lines[x][-1] == '\n'):
            st= lines[x]
    
    viewbox=str(st[:-1])
    
    with open('DiagramTitles.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] == filename + '.svg':
                aria_label = row[1]
                aria_desc = row[2]
    
    
    o.write('<html>\n')
    o.write('<head>\n')
    o.write('  <link rel="stylesheet" type="text/css" href="https://planetearth.utsc.utoronto.ca/diagrams/tooltipster.bundle.min.css"/>\n')
    o.write('  <link rel="stylesheet" type="text/css" href="https://planetearth.utsc.utoronto.ca/diagrams/tooltipster-follower.min.css"/>\n')
    o.write('  <link rel="stylesheet" type="text/css" href="https://planetearth.utsc.utoronto.ca/diagrams/style.css?v=1.1"/>\n')
    o.write('  <script type="text/javascript" src="https://code.jquery.com/jquery-1.10.0.min.js"></script>\n')
    o.write('  <script type="text/javascript" src="https://planetearth.utsc.utoronto.ca/diagrams/tooltipster.bundle.min.js"></script>\n')
    o.write('  <script type="text/javascript" src="https://planetearth.utsc.utoronto.ca/diagrams/tooltipster-follower.min.js"></script>\n')
    o.write('  <script>\n')
    o.write('  $(document).ready(function() {\n')
    o.write("      $('.tooltip').tooltipster({\n")
    o.write("      plugins: ['follower'],\n")
    o.write("      contentAsHTML: true,\n")
    o.write("      trigger: 'custom', // add custom trigger\n")
    o.write("       triggerOpen: { // open tooltip when element is clicked, tapped (mobile) or hovered\n")
    o.write("           click: true,\n")
    o.write("           tap: true,\n")
    o.write("           mouseenter: true\n")
    o.write("           },\n")
    o.write("          triggerClose: { // close tooltip when element is clicked again, tapped or when the mouse leaves it\n")
    o.write("           click: true,\n")
    o.write("           scroll: false, // ensuring that scrolling mobile is not tapping!\n")
    o.write("           tap: true,\n")
    o.write("           mouseleave: true\n")
    o.write("           }\n")
    o.write("     \n" )
    o.write("  });\n")
    o.write("  });\n")
    o.write("</script>\n")
    o.write("\n")
    o.write("</head>\n")
    o.write("\n")
    o.write("<body>\n")
    o.write('  <a href="full.html" target="_blank">\n')
    o.write('    <img src="https://planetearth.utsc.utoronto.ca/diagrams/media-fullscreen.png" alt="Expand image" id="expandfull">\n')
    o.write("  </a>\n")
    o.write('<div class="container">\n')
    stforlin= '<svg id="InteractiveFigure" height="100%" width="100%" ' + viewbox + ' version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-label="'+aria_label+'" aria-describedby="map-desc" role="group">\n'
    o.write(stforlin)
    st2forlin = '    <desc id="map-desc">'+aria_desc+'</desc>\n'
    o.write(st2forlin)
    
    
    ################################################################################################################
    start_writing=False
    starting_line = re.compile('g id')
    counts= 1
    
    for line in lines:
        m = prog.search(line)
        m2 = starting_line.search(line)
        if m2:
            start_writing = True
        if m:
            #print( line )
            path_id = m.group()
            path_id = path_id.strip('path id=').strip('\"').strip()
            new_line = ''
            for row in tab:
                pid = row[1]
                #if path_id == 'Cordillera':
                #    pdb.set_trace()
                if  pid == path_id:
                    new_string = 'path class="tooltip" title="<strong>%s</strong><br>%s" xlink:href="#%s" role="img" aria-label="%s" tabindex="%s" '%(row[2], row[3], row[1], row[5], counts)
                    counts = counts + 1
                    new_line = re.sub('path', new_string, line)
            if start_writing:
                if new_line == '':
                    o.write(line)
                else:
                    o.write(new_line)
        else:
            if start_writing: 
                o.write(line)
    #################################################################################################################
    o.write('\n')
    o.write('</div>\n')
    o.write('</body>\n')
    o.write('</html>\n')

def fullmaker( foldername,filename ):
    ### Input Parameters ###########################################################################################
    infile = foldername + '/' + filename + '.svg'
    try:
        os.makedirs(foldername + '/' + filename)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
            
    outfile_name = foldername + '/' + filename + '/full.html'
    
    ################################################################################################################
    
    table = open( foldername + '/' +'Labels.csv', 'r'  ).readlines()
    tab = []
    
    for line in table:
        sline = line.strip().split(',')
        tab.append(sline)
    
    
    prog = re.compile('path id=.*?" ')
    
    lines = open(infile, 'r').readlines()
    o = open(outfile_name, 'w')
    
    #############################################################################################################
    for x in range(len(lines)):
        if (lines[x][0]+lines[x][1]+lines[x][2]+lines[x][3] == 'view') and (lines[x][-1] == '\n'):
            st= lines[x]
    
    viewbox=str(st[:-1])
    
    with open('DiagramTitles.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] == filename + '.svg':
                aria_label = row[1]
                aria_desc = row[2]
            
    
    o.write('<html>\n')
    o.write('<head>\n')
    o.write('  <link rel="stylesheet" type="text/css" href="https://planetearth.utsc.utoronto.ca/diagrams/tooltipster.bundle.min.css"/>\n')
    o.write('  <link rel="stylesheet" type="text/css" href="https://planetearth.utsc.utoronto.ca/diagrams/tooltipster-follower.min.css"/>\n')
    o.write('  <link rel="stylesheet" type="text/css" href="https://planetearth.utsc.utoronto.ca/diagrams/style.css?v=1.1"/>\n')
    o.write('  <script type="text/javascript" src="https://code.jquery.com/jquery-1.10.0.min.js"></script>\n')
    o.write('  <script type="text/javascript" src="https://planetearth.utsc.utoronto.ca/diagrams/tooltipster.bundle.min.js"></script>\n')
    o.write('  <script type="text/javascript" src="https://planetearth.utsc.utoronto.ca/diagrams/tooltipster-follower.min.js"></script>\n')
    o.write('  <script>\n')
    o.write('  $(document).ready(function() {\n')
    o.write("      $('.tooltip').tooltipster({\n")
    o.write("      plugins: ['follower'],\n")
    o.write("      contentAsHTML: true,\n")
    o.write("      trigger: 'custom', // add custom trigger\n")
    o.write("       triggerOpen: { // open tooltip when element is clicked, tapped (mobile) or hovered\n")
    o.write("           click: true,\n")
    o.write("           tap: true,\n")
    o.write("           mouseenter: true\n")
    o.write("           },\n")
    o.write("          triggerClose: { // close tooltip when element is clicked again, tapped or when the mouse leaves it\n")
    o.write("           click: true,\n")
    o.write("           scroll: false, // ensuring that scrolling mobile is not tapping!\n")
    o.write("           tap: true,\n")
    o.write("           mouseleave: true\n")
    o.write("           }\n")
    o.write("     \n" )
    o.write("  });\n")
    o.write("  });\n")
    o.write("</script>\n")
    o.write("\n")
    o.write("</head>\n")
    o.write("\n")
    o.write("<body>\n")
    o.write('<div class="container">\n')
    stforlin= '<svg id="InteractiveFigure" height="100%" width="100%" ' + viewbox + ' version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-label="'+aria_label+'" aria-describedby="map-desc" role="group">\n'
    o.write(stforlin)
    st2forlin = '    <desc id="map-desc">'+aria_desc+'</desc>\n'
    o.write(st2forlin)
    
    
    ################################################################################################################
    start_writing=False
    starting_line = re.compile('g id')
    counts = 1
    for line in lines:
        m = prog.search(line)
        m2 = starting_line.search(line)
        if m2:
            start_writing = True
        if m:
            #print( line )
            path_id = m.group()
            path_id = path_id.strip('path id=').strip('\"').strip()
            new_line = ''
            for row in tab:
                pid = row[1]
                #if path_id == 'Cordillera':
                #    pdb.set_trace()
                if  pid == path_id:
                    new_string = 'path class="tooltip" title="<strong>%s</strong><br>%s" xlink:href="#%s" role="img" aria-label="%s" tabindex="%s" '%(row[2], row[3], row[1], row[5], counts)
                    counts = counts + 1
                    new_line = re.sub('path', new_string, line)
            if start_writing:
                if new_line == '':
                    o.write(line)
                else:
                    o.write(new_line)
        else:
            if start_writing: 
                o.write(line)
    #################################################################################################################
    o.write('\n')
    o.write('</div>\n')
    o.write('</body>\n')
    o.write('</html>\n')









