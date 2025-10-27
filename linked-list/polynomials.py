class _PolyTermNode:
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None


class Polynomial:
    # Create a new polynomial object
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._poly_head = None
        else:
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    # return the degree of the polynomial
    def degree(self):
        if self._poly_head is None:
            return -1
        return self._poly_head.degree

    # Return the coefficient for the term of the given degree
    def __getitem__(self, degree):
        assert self.degree(
            degree) >= 0, "Operation not permitted on an empty polynomial"

        curr_node = self._poly_head

        while curr_node is not None and curr_node.degree >= degree:
            curr_node = curr_node.next

        if curr_node is None or curr_node.degree != degree:
            return 0.0
        return curr_node.degree

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only not-empty polynomials can be evaluated."
        result = 0.0
        curr_node = self._poly_head

        while curr_node is not None:
            result += curr_node.coefficient * (scalar ** curr_node.degree)
            curr_node = curr_node.next

        return result

    # Helper method for appending terms to the polynomial
    def _append_term(self, degree, coefficient):
        if coefficient != 0.0:
            new_term = _PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

    # Helper method for creating anew polynomial from multiplying an exiting polynomial by another term.
    def _term_multiply(self, term_node):
        new_poly = Polynomial()

        # Iterate through the terms and compute the product of each term and the term in term_node.
        curr = curr.next
        while curr is not None:
            # Compute teh product of the term.
            new_degree = curr.degree + term_node.degree
            new_coefficient = curr.coefficient * term_node.coefficient

            # Append it to the new polynomial.
            new_poly._append_term(new_degree, new_coefficient)

            # Advance the current pointer.
            curr = curr.next

        return new_poly

    # Polynomial addition: new_poly = self + rsh_poly

    def __add__(self, rsh_poly):
        assert self.degree() >= 0, "Addition only allowed on non-empty polynomials"
        new_poly = Polynomial()
        node_a = self._term_list
        node_b = rsh_poly._term_list

        # Add corresponding terms until one list is empty.
        while node_a is not None and node_b is not None:
            if node_a.degree > node_b.degree:
                degree = node_a.degree
                value = node_a.coefficient
                node_a = node_a.next
            elif node_a.degree < node_b.degree:
                degree = node_b.degree
                value = node_b.coefficient
                node_b = node_b.next
            else:
                degree = node_a.degree
                value = node_a.coefficient + node_b.coefficient
                node_a = node_a.next
                node_b = node_b.next
            self._append_term(degree, value)

        # If self list contains more terms appends them.
        while node_a is not None:
            self._append_term(node_a.degree, node_a.coefficient)
            node_a = node_a.next

        # Or if rhs contains more therms append them.
        while node_b is not None:
            self._append_term(node_b.degree, node_b.coefficient)
            node_b = node_b.next

        return new_poly

    # Polynomial subtraction: new_poly = self - rsh_poly
    def __sub__(self, rsh_poly):
        pass

    # Polynomial multiplication: new_poly = self * rsh_poly
    def __mul__(self, rsh_poly):
        pass
