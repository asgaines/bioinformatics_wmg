import argparse

import matplotlib.pyplot as plt


def plot_data(fname: str, label: str):
    with open(fname, 'r') as f:
        cvg_data = [line.rstrip().split('\t') for line in f.readlines()]
    
    gene_anns = [line[3].split('_')[1] for line in cvg_data]
    read_depth = [int(line[6]) for line in cvg_data]

    plt.plot(gene_anns, read_depth, label=label)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visualize results of read depth coverage')
    parser.add_argument('baseline', type=str, help='Path to coverage file for baseline reads')
    parser.add_argument('variant', type=str, help='Path to coverage file for variant reads')
    parser.add_argument('out', type=str, help='Filename for output visualization graph')
    args = parser.parse_args()

    plot_data(args.baseline, 'baseline')
    plot_data(args.variant, 'variant')

    plt.xticks(rotation=90)

    plt.legend()
    plt.xlabel('gene #')
    plt.ylabel('read depth')
    plt.grid(visible=True)

    plt.savefig(args.out)
    print(f'Saved visualization to {args.out}')