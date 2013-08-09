import re
import argparse
import os

def make_italic_dict(replace_list):
    
    i_dic = {}
    
    for word in replace_list:
        exp = r'(?<!\{)('+word+r')(?!\})'
        i_dic[word] = re.compile(exp)
        
    return i_dic

def do_italic(infile, outfile, r_dic):
    tmpfile = '~'+infile[0:infile.rfind('.')]+'.tmp'
    
    if outfile == '' or outfile == infile: outfile = tmpfile
    
    fin = open(infile,'r')
    fout = open(outfile,'w')
    
    for line in fin:
        for word in r_dic:
            line = r_dic[word].sub(r'\\textit{'+word+'}', line)
        fout.write(line)
    
    fout.close()
    fin.close()
    
    if outfile == tmpfile:
        os.remove(infile)
        os.rename(outfile, infile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('-o','--outfile', default = '')
    parser.add_argument('-i','--italic', nargs='+')
    
    args = parser.parse_args()
    
    italic_dict = make_italic_dict(args.italic)
    do_italic(args.infile, args.outfile, italic_dict)