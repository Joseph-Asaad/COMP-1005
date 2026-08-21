class AbsRepr :
  def __repr__(self):
    return str(vars(self))