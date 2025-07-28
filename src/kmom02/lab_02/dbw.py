"""
Detta modul innehåller verktyg för att köra tester, samla statistik och skriva ut resultat.
"""

import sys


class Statistic:
    """
    Klass för att hålla statistik om varje metods testresultat.
    """

    def __init__(self, points):
        self.run_count = 0
        self.passed = 0
        self.failed = 0
        self.points = points

    def run(self, success):
        self.run_count += 1
        if success:
            self.passed += 1
        else:
            self.failed += 1


class DBW:
    """
    Klass med statisk funktionalitet för assertion och testresultat.
    """

    PASS = 15
    PASS_W_HONOUR = 19
    PASS_TOTAL = 21

    stats = {}

    @staticmethod
    def feedback(points):  # noqa: C901
        """
        Returnerar en sträng med motiverande feedback beroende på antal poäng.
        """
        msg = "Great, you are on fire and progress is made. 😋"
        if points == 0:
            msg = "Try to earn 1 point to get started... 😏"
        elif points == 1:
            msg = "Nice work, lets go, do another! 😉"
        elif points == DBW.PASS - 3:
            msg = "Just three more to PASS. Lets go. 😅"
        elif points == DBW.PASS - 2:
            msg = "Just two more to PASS. Lets go. 😅"
        elif points == DBW.PASS - 1:
            msg = "Just one more to PASS. Lets go. 😅"
        elif points == DBW.PASS:
            msg = "Excellent, you have PASSED. One more? 😁"
        elif points == DBW.PASS_W_HONOUR - 2:
            msg = "Two more to PASS WITH HONOUR! Lets go. 😅"
        elif points == DBW.PASS_W_HONOUR - 1:
            msg = "One more to PASS WITH HONOUR! Lets go. 😅"
        elif points == DBW.PASS_W_HONOUR:
            msg = "That is the way, you PASSED WITH HONOUR! 😍"
        elif points == DBW.PASS_TOTAL:
            msg = "What can I say. You impress me. 🙌"
        return msg

    @staticmethod
    def assert_(func, args, expected, points=1):
        """
        Kör ett testfall och skriver ut resultat samt uppdaterar statistik.
        """
        try:
            result = func(*args)
        except Exception as error:  # noqa: BLE001
            print("💥 Error:", error)
            result = None

        success = result == expected
        method_name = func.__name__

        if method_name not in DBW.stats:
            DBW.stats[method_name] = Statistic(points)

        DBW.stats[method_name].run(success)

        success_str = "✅" if success else "❌"
        points_earned = DBW.stats[method_name].points
        args_str = DBW.args_as_string(args)

        msg = (
            f"{success_str} {points_earned}p. {method_name}({args_str}), expected: "
            f"{DBW.format_value(expected)}, actual: {DBW.format_value(result)}"
        )
        print(msg)

    @staticmethod
    def format_value(arg):
        if isinstance(arg, list):
            return f"[{', '.join(map(str, arg))}]"
        elif isinstance(arg, str):
            return f'"{arg}"'
        else:
            return str(arg)

    @staticmethod
    def args_as_string(args):
        """
        Returnerar en strängrepresentation av funktionsargument.
        """
        return ", ".join(DBW.format_value(a) for a in args)

    @staticmethod
    def done():
        """
        Skriver ut sammanfattning av alla tester.
        """
        passed = failed = total = result = 0
        point_array = [False] * DBW.PASS_TOTAL
        step = 0

        for stat in DBW.stats.values():
            passed += stat.passed
            failed += stat.failed
            total += stat.passed + stat.failed
            result += 0 if stat.failed > 0 else stat.points * stat.passed

            for _ in range(stat.points):
                # if step < len(point_array):
                step += 1
                point_array[step] = stat.failed == 0

        def format_point(i, pass_):
            if pass_:
                return " ⦿ "
            elif i + 1 == DBW.PASS:
                return " 😁 "
            elif i + 1 == DBW.PASS_W_HONOUR:
                return " 😍 "
            elif i + 1 == DBW.PASS_TOTAL:
                return " 🙌 "
            else:
                return " ⦾ "

        point_str = "".join(format_point(i, p) for i, p in enumerate(point_array))

        summary = f"""
--------------------------------------------------------------------
| Total: {total}, Passed ✅: {passed}, Failed ❌: {failed}
| Points needed to PASS={DBW.PASS}, PASS WITH HONOUR={DBW.PASS_W_HONOUR}, TOTAL={DBW.PASS_TOTAL}
|{point_str}
|
| You have {result} points. {DBW.feedback(result)}
--------------------------------------------------------------------
"""
        print(summary)

        if result >= DBW.PASS:
            sys.exit(0)
        sys.exit(1)
