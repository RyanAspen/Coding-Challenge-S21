#This code makes use of the GenomeDiagram module
#It also closely follows the format of the tutorial on https://www.tutorialspoint.com/biopython/biopython_genome_analysis.htm

#Import Libraries
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

#Get data record from genbank file
record = SeqIO.read("Genome.gb", "genbank")

#Create objects for GenomeDiagram library
diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
track = diagram.new_track(1, name="Important Features")
features = track.new_set()

#Change features so that they are more easily distinguishable
for feature in record.features:
    if feature.type != "gene":
        continue
    if len(feature) % 2 == 0:
        feature_color = colors.blue
    else:
        feature_color = colors.red

    #Add formatted feature to features object
    features.add_feature(feature, color=feature_color, label=True)

#Draw the diagram in a circular format
diagram.draw(format = "circular", circular=True, pagesize = (20*cm, 20*cm), start = 0, end = len(record), circle_core = 0.7)

#Output the diagram as a PNG file
diagram.write("circularGenomeMap.png", "PNG")