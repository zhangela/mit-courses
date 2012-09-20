from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    print hypothesis
    for rule in rules:
        consequent = rule.consequent()
        for expr in consequent:
            bindings = match(expr, hypothesis)
            if bindings:
                antecedent = rule.antecedent()
                if isinstance(antecedent, str):
                    return antecedent
                else:
                    statements = [populate(ante_expr, bindings) for ante_expr in antecedent]
                    secondary_results = []
                    for statement in statements:
                        secondary_results.append(backchain_to_goal_tree(rules, statement))
                    return create_statement(results, antecedent)
    print 'finished ' + hypothesis
    return results

def create_statement(statements, rule):
    if isinstance(rule, AND):
        return AND(statements)
    elif isinstance(rule, OR):
        return OR(statements)

# Here's an example of running the backward chainer - uncomment
# it to see it work:
print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')