from bf1chs import BF1ChsToolbox


def main():
    try:
        BF1ChsToolbox().run()
    except BF1ChsToolbox.ExitException:
        pass


if __name__ == "__main__":
    main()
