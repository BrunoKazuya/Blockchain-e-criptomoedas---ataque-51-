"""
simulate_attack51.py
Simulação didática e realista off-chain do Ataque 51%.
"""
import argparse
import random
import numpy as np
import matplotlib.pyplot as plt



def sample_run(p=0.55, steps=200, seed=None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    attacker_private = 0
    honest_public = 0

    att_hist = []
    hon_hist = []
    events = []

    for t in range(steps):
        if random.random() < p:
            attacker_private += 1
        else:
            honest_public += 1

        if attacker_private > honest_public:
            honest_public = attacker_private
            events.append((t, f"reorg at step {t}: attacker revealed {attacker_private}"))
            attacker_private = 0

        att_hist.append(attacker_private)
        hon_hist.append(honest_public)

    return att_hist, hon_hist, events



def trial_double_spend(p=0.51, k=6, trials=10000, seed=None):
    if seed is not None:
        random.seed(seed)

    successes = 0

    for _ in range(trials):
        attacker = 0
        honest = 0

        while honest < k:
            if random.random() < p:
                attacker += 1
            else:
                honest += 1

        if attacker > honest:
            successes += 1
            continue

        max_steps = 10000
        for _ in range(max_steps):
            if random.random() < p:
                attacker += 1
            else:
                honest += 1

            if attacker > honest:
                successes += 1
                break

            if honest - attacker > 10 * k:
                break

    return successes / trials


def trial_double_spend_realistic(p=0.51, k=6, trials=10000, seed=None):
    """
    Modelo mais próximo de redes reais:
    - Honest chega a k confirmações primeiro
    - Atacante só começa a corrida depois disso
    - Tempo limitado para perseguição
    """

    if seed is not None:
        random.seed(seed)

    successes = 0

    for _ in range(trials):
        honest = k
        attacker = 0

        max_steps = 1000

        for _ in range(max_steps):
            if random.random() < p:
                attacker += 1
            else:
                honest += 1

            if attacker >= honest:
                successes += 1
                break

            if honest - attacker > 10 * k:
                break

    return successes / trials


def approx_satoshi_prob(p, k):
    if p >= 0.5:
        return 1.0
    q = p
    return (q / (1 - q)) ** k



def plot_sample(att_hist, hon_hist, events, out_path=None):
    steps = range(len(att_hist))
    plt.figure(figsize=(10, 4))
    plt.plot(steps, att_hist, label='attacker_private_len')
    plt.plot(steps, hon_hist, label='honest_public_len')

    for (t, ev) in events:
        plt.axvline(t, linestyle='--', linewidth=0.7)
        ymax = max(hon_hist[t], att_hist[t])
        plt.text(t, ymax + 0.3, 'reorg', rotation=90, fontsize=8)

    plt.xlabel('step')
    plt.ylabel('chain length (relative)')
    plt.title('Sample evolution - attacker vs honest')
    plt.legend()
    plt.tight_layout()

    if out_path:
        plt.savefig(out_path, bbox_inches='tight')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['sample', 'batch'], default='sample')
    parser.add_argument('--model', choices=['didactic', 'realistic'], default='didactic',
                        help="Escolhe qual modelo usar no modo batch.")
    parser.add_argument('--p', type=float, default=0.55)
    parser.add_argument('--steps', type=int, default=200)
    parser.add_argument('--k', type=int, default=6)
    parser.add_argument('--trials', type=int, default=2000)
    parser.add_argument('--seed', type=int, default=None)
    args = parser.parse_args()

    if args.mode == 'sample':
        att_hist, hon_hist, events = sample_run(
            p=args.p, steps=args.steps, seed=args.seed
        )
        plot_sample(att_hist, hon_hist, events, out_path='sample_evolution.png')
        print("Sample run concluída. Gráfico salvo como sample_evolution.png")

    else:
        if args.model == 'didactic':
            prob_sim = trial_double_spend(
                p=args.p, k=args.k, trials=args.trials, seed=args.seed
            )
        else:
            prob_sim = trial_double_spend_realistic(
                p=args.p, k=args.k, trials=args.trials, seed=args.seed
            )

        prob_teo = approx_satoshi_prob(args.p, args.k)

        print(f"\nModelo: {args.model}")
        print(f"Simulação    p={args.p:.3f}, k={args.k}, trials={args.trials}: {prob_sim:.4f}")
        print(f"Teórica aprox p={args.p:.3f}, k={args.k}: {prob_teo:.4f}\n")
