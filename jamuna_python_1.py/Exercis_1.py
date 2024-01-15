class i:
    def __init__(self, n, p):
        self.n = n
        self.p = p


class ORDER:
    def __init__(self):
        self.its = []

    def AddItem(self, i, q):
        self.its.append({"i": i, "q": q})

    def total(self):
        t = 0
        for item in self.its:
            t += item["i"].p * item["q"]
        return t


class billgenerator:
    def __init__(self, order):
        self.order = order

    def generate_bill(self):
        ta = self.order.total()
        st = 0.05 * ta  # Assuming 5% service tax
        gst = 0.18 * ta  # Assuming 18% GST

        fa = ta + st + gst

        # Display the bill
        print("------ Bill ------")
        for item in self.order.its:
            print(f"{item['i'].n} x {item['q']}: {item['i'].p * item['q']}")

        print(f"\nTotal Amount: {ta}")
        print(f"Service Tax (5%): {st}")
        print(f"GST (18%): {gst}")
        print(f"Final Amount: {fa}")


# Example usage:
item1 = i("item1", 10.0)
item2 = i("item2", 15.0)

order = ORDER()
order.AddItem(item1, 2)
order.AddItem(item2, 1)

bill_generator = billgenerator(order)
bill_generator.generate_bill()
