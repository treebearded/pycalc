import argparse

def calculate_dots_in_figure(n):
    """
    Kalkulerer antall prikker i figur nummer n.
    Formelen er S_n = (n+2)^2 + n^2 = 2n^2 + 4n + 4.
    """
    return 2 * n**2 + 4 * n + 4

def calculate_figures_from_total_dots(total_dots_limit):
    """
    Kalkulerer hvor mange figurer man kan lage med et gitt totalt antall prikker.
    Itererer og summerer prikker fra figur 1 og oppover til summen overstiger grensen.
    """
    current_sum = 0
    num_figures = 0
    while True:
        # Kalkuler prikker for neste figur
        dots_in_next_figure = calculate_dots_in_figure(num_figures + 1)

        # Sjekk om adding av neste figur vil overskride grensen
        if current_sum + dots_in_next_figure <= total_dots_limit:
            current_sum += dots_in_next_figure
            num_figures += 1
        else:
            # Hvis neste figur overskrider grensen, kan vi ikke lage den.
            # Vi har funnet maksimalt antall figurer.
            break
    return num_figures, current_sum

def main():
    parser = argparse.ArgumentParser(
        description="Kalkulator for rektangeltall. "
                    "Beregner enten antall prikker i en spesifikk figur "
                    "eller antall figurer som kan lages med et gitt antall prikker."
    )
    # Legger til argument for figur-nummer (-f)
    parser.add_argument(
        "-f", "--figure",
        type=int,
        help="Angi figur-nummer for å beregne antall prikker i den figuren."
    )
    # Legger til argument for totalt antall prikker (-p)
    parser.add_argument(
        "-p", "--points",
        type=int,
        help="Angi totalt antall prikker for å beregne hvor mange figurer som kan lages."
    )

    args = parser.parse_args()

    # Sjekker hvilken modus brukeren har valgt
    if args.figure is not None:
        if args.figure <= 0:
            print("Feil: Figur-nummer må være et positivt heltall.")
        else:
            dots = calculate_dots_in_figure(args.figure)
            print(f"Figur {args.figure} har {dots} prikker.")
    elif args.points is not None:
        if args.points < calculate_dots_in_figure(1):
            print(f"Feil: Du trenger minst {calculate_dots_in_figure(1)} prikker for å lage én figur.")
        else:
            num_figures, total_dots_used = calculate_figures_from_total_dots(args.points)
            print(f"Med {args.points} prikker kan du lage {num_figures} figurer.")
            print(f"Totalt antall prikker brukt for {num_figures} figurer er {total_dots_used}.")
    else:
        # Hvis ingen argumenter er spesifisert, viser hjelpetekst
        parser.print_help()

if __name__ == "__main__":
    main()
